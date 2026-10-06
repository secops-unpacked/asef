import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import reference as ref
import validate
import catalogue_docs


class TechnologyTests(unittest.TestCase):
    def setUp(self):
        self.doc = ref.load_json(ROOT / "examples/technology-evaluation.json")
        self.caps = ref.catalogue()

    def one(self, availability="ga_out_of_box", rating="0", platform=False):
        doc = copy.deepcopy(self.doc)
        cid = "platform.ops.close-alerts-siem" if platform else "mid.enrich.external-ti"
        doc["capabilityIds"] = [cid]
        doc["assessments"] = [{"capabilityId": cid, "availability": availability, "evaluator": rating}]
        return doc

    def test_worked_example(self):
        overall = ref.technology_scores(self.doc)["overall"]
        self.assertEqual(overall["rated"], 4)
        self.assertEqual(overall["ratedDepthPct"], 37.5)
        self.assertEqual(overall["gaCoveragePct"], 60)
        self.assertEqual(overall["fullAutomationPct"], 25)

    def test_manual_ga_is_present_not_autonomous(self):
        overall = ref.technology_scores(self.one())["overall"]
        self.assertEqual(overall["gaCoveragePct"], 100)
        self.assertEqual(overall["ratedDepthPct"], 0)
        self.assertEqual(overall["fullAutomationPct"], 0)

    def test_ga_delivery_paths_remain_distinct(self):
        for delivery in ref.GA:
            with self.subTest(delivery=delivery):
                result = ref.technology_scores(self.one(delivery, "2"))["overall"]
                self.assertEqual(result["gaCoveragePct"], 100)
                self.assertEqual(result["deliveryCounts"], {delivery: 1})

    def test_preview_and_roadmap_are_not_current(self):
        for delivery in ("public_roadmap", "private_preview", "public_preview"):
            with self.subTest(delivery=delivery):
                result = ref.technology_scores(self.one(delivery, "2"))["overall"]
                self.assertIsNone(result["ratedDepthPct"])
                self.assertEqual(result["gaCoveragePct"], 0)
                self.assertEqual(result["fullAutomationPct"], 0)

    def test_unsupported_forces_zero(self):
        result = ref.technology_scores(self.one("not_supported", "2"))["overall"]
        self.assertEqual(result["ratedDepthPct"], 0)
        self.assertEqual(result["levelCounts"], {"0": 1})

    def test_unrecorded_delivery_is_flagged_not_ga(self):
        result = ref.technology_scores(self.one(None, "2"))
        self.assertEqual(result["overall"]["ratedDepthPct"], 100)
        self.assertEqual(result["overall"]["gaCoveragePct"], 0)
        self.assertEqual(result["unconfirmedDeliveryRatings"], ["mid.enrich.external-ti"])

    def test_unanswered_is_unknown(self):
        doc = self.one()
        doc["assessments"] = []
        result = ref.technology_scores(doc)["overall"]
        self.assertIsNone(result["ratedDepthPct"])
        self.assertEqual(result["rated"], 0)
        self.assertEqual(result["deliveryCounts"], {"unknown": 1})

    def test_scoped_denominator(self):
        result = ref.technology_scores(self.one(rating="2"))["overall"]
        self.assertEqual(result["inScope"], 1)
        self.assertEqual(result["fullAutomationPct"], 100)

    def test_functional_support_not_autonomy(self):
        result = ref.technology_scores(self.one(rating="1", platform=True))["overall"]
        self.assertEqual(result["ratedDepthPct"], 50)
        self.assertEqual(result["gaCoveragePct"], 100)
        self.assertIsNone(result["fullAutomationPct"])

    def test_platform_zero_not_covered_and_warning(self):
        result = ref.technology_scores(self.one(platform=True))
        self.assertEqual(result["overall"]["gaCoveragePct"], 0)
        self.assertTrue(result["platformWarning"])

    def test_platform_unrated_does_not_claim_pass(self):
        result = ref.technology_scores(self.one(rating=None, platform=True))
        self.assertIsNone(result["zones"]["platform"]["ratedDepthPct"])
        self.assertEqual(result["zones"]["platform"]["rated"], 0)

    def test_empty_selection(self):
        self.doc["capabilityIds"], self.doc["assessments"] = [], []
        result = ref.technology_scores(self.doc)["overall"]
        self.assertIsNone(result["ratedDepthPct"])
        self.assertIsNone(result["fullAutomationPct"])

    def test_rating_variants(self):
        for rating in ("1C", "1G", "1A"):
            with self.subTest(rating=rating):
                self.assertEqual(ref.technology_scores(self.one(rating=rating))["overall"]["ratedDepthPct"], 50)

    def test_invalid_scale_codes(self):
        for rating, platform in [("1", False), ("1G", True), (True, False), (2, False), ("3", False)]:
            with self.subTest(rating=rating, platform=platform), self.assertRaises(ValueError):
                ref.technology_scores(self.one(rating=rating, platform=platform))

    def test_invalid_inputs(self):
        variants = []
        for key, value in [("track", "mdr"), ("frameworkVersion", "2.0.0"), ("schemaVersion", True), ("capabilityIds", ["unknown"])]:
            doc = copy.deepcopy(self.doc)
            doc[key] = value
            variants.append(doc)
        doc = copy.deepcopy(self.doc)
        doc["capabilityIds"].append(doc["capabilityIds"][0])
        variants.append(doc)
        doc = copy.deepcopy(self.doc)
        doc["assessments"].append(doc["assessments"][0])
        variants.append(doc)
        doc = copy.deepcopy(self.doc)
        doc["unexpected"] = "not an importer"
        variants.append(doc)
        for doc in variants:
            with self.subTest(document=doc), self.assertRaises(ValueError):
                ref.technology_scores(doc)

    def test_rounding_matches_decimal_half_up(self):
        self.assertEqual(ref.percent(1, 32), 3.1)
        self.assertEqual(ref.percent(1, 16), 6.3)
        self.assertEqual(ref.percent(1, 3), 33.3)


class NeedsTests(unittest.TestCase):
    def setUp(self):
        self.doc = ref.load_json(ROOT / "examples/needs-comparison.json")

    def first(self):
        return ref.needs_comparison(self.doc)["offerings"][0]

    def test_worked_example(self):
        a, b = ref.needs_comparison(self.doc)["offerings"]
        self.assertEqual([a[k] for k in ("met", "partial", "unmet", "unknown")], [1, 1, 0, 1])
        self.assertEqual([b[k] for k in ("met", "partial", "unmet", "unknown")], [2, 0, 1, 0])

    def test_vendor_claim_is_unknown(self):
        for finding in self.doc["offerings"][0]["findings"]:
            finding["evidenceBasis"] = "vendor_claim"
        self.assertEqual(self.first()["unknown"], 3)

    def test_blank_evidence_is_unknown(self):
        self.doc["offerings"][0]["findings"][0]["evidenceReference"] = "  "
        self.assertEqual(self.first()["unknown"], 2)

    def test_changed_criterion_invalidates_outcome(self):
        self.doc["criteria"][0]["successCriterion"] += " Additional constraint."
        self.assertEqual(self.first()["unknown"], 2)

    def test_changed_context_is_stale(self):
        for field, value in [("needsId", "other"), ("profileId", "other"), ("profileRevision", 2), ("track", "mdr")]:
            doc = copy.deepcopy(self.doc)
            doc["offerings"][0]["reviewContext"][field] = value
            result = ref.needs_comparison(doc)["offerings"][0]
            with self.subTest(field=field):
                self.assertTrue(result["stale"])
                self.assertEqual(result["unknown"], 3)

    def test_new_profile_revision_invalidates_old_review(self):
        self.doc["offerings"][0]["revision"] += 1
        self.assertTrue(self.first()["stale"])
        self.assertEqual(self.first()["unknown"], 3)

    def test_no_context_not_evidence(self):
        self.doc["offerings"][0]["reviewContext"] = None
        self.assertEqual(self.first()["unknown"], 3)

    def test_only_must_haves_count(self):
        for priority in ("nice", "explore", "out"):
            self.doc["criteria"][0]["priority"] = priority
            with self.subTest(priority=priority):
                self.assertEqual(self.first()["mustHaves"], 2)
                self.assertEqual(self.first()["met"], 0)

    def test_no_must_haves_not_full_match(self):
        for criterion in self.doc["criteria"]:
            criterion["priority"] = "out"
        self.assertEqual(self.first()["mustHaves"], 0)
        self.assertEqual(sum(self.first()[k] for k in ("met", "partial", "unmet", "unknown")), 0)

    def test_mdr_separate_track(self):
        doc = ref.load_json(ROOT / "examples/mdr-comparison.json")
        result = ref.needs_comparison(doc)
        self.assertEqual(result["track"], "mdr")
        self.assertEqual([result["offerings"][0][k] for k in ("met", "partial", "unmet", "unknown")], [1, 1, 0, 1])

    def test_mixed_tracks_rejected(self):
        self.doc["track"] = "mdr"
        with self.assertRaises(ValueError):
            self.first()

    def test_boolean_outcome_rejected(self):
        self.doc["offerings"][0]["findings"][0]["outcome"] = True
        with self.assertRaises(ValueError):
            self.first()

    def test_unknown_and_duplicate_findings_rejected(self):
        for cid in ("not-a-criterion", "research.right.endpoint"):
            self.doc["offerings"][0]["findings"][0]["criterionId"] = cid
            with self.subTest(cid=cid), self.assertRaises(ValueError):
                self.first()


class RepositoryTests(unittest.TestCase):
    def test_definitions_and_counts(self):
        self.assertEqual(validate.definitions()["technologyCapabilities"], 111)

    def test_generated_documents_are_current(self):
        self.assertEqual(catalogue_docs.check(), [])

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.json"
            path.write_text('{"key": 1, "key": 2}', encoding="utf-8")
            with self.assertRaises(ValueError):
                ref.load_json(path)

    def test_link_checker(self):
        path = ROOT / "README.md"
        self.assertEqual(validate.local_links("[Guide](docs/guide.md) [Web](https://example.com) [Anchor](#local)", path), [])
        self.assertEqual(len(validate.local_links("[Bad](docs/absent-file.md)", path)), 1)
        self.assertEqual(len(validate.local_links("[Outside](../outside.md)", path)), 1)
        self.assertEqual(len(validate.local_links("[[Nested](https://example.com)](https://example.com)", path)), 1)

    def test_cli_public_example(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/reference.py"), str(ROOT / "examples/technology-evaluation.json")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["kind"], "technology-summary")

    def test_cli_rejects_unknown_document(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/reference.py"), str(ROOT / "data/manifest.json")], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Invalid evaluation", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
