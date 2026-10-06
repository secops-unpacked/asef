# Fictional worked examples

All names, scenarios and evidence references here are invented. They are not vendor evaluations or templates prefilled with verified claims.

## Technology capability profile

```sh
python3 scripts/reference.py examples/technology-evaluation.json
```

Five checks are in scope. Two lifecycle checks are GA, one is preview, one is unsupported, and one Platform and Trust check is partially supported and GA.

- GA coverage: 3/5 = **60%**.
- Rated depth: 3 points across 4 rated checks = **37.5%**.
- Full lifecycle automation: 1/4 = **25%**.
- The manual enrichment check counts as GA capability but adds no autonomy points.
- The end-to-end timeline requires a customer build. Its automation level does not make it out of the box.
- The preview investigation claim does not count toward current GA coverage or rated depth.

## Needs-based technology comparison

```sh
python3 scripts/reference.py examples/needs-comparison.json
```

| Offering | Met | Partial | Unmet | Unknown |
| --- | --- | --- | --- | --- |
| Example Technology A | 1 | 1 | 0 | 1 |
| Example Technology B | 2 | 0 | 1 | 0 |

Both are assessed against the same three must-haves. A vendor statement remains Unknown even if someone enters outcome `2`. B's unmet requirement cannot be hidden by its two met requirements. There is no automatic winner.

## MDR comparison

```sh
python3 scripts/reference.py examples/mdr-comparison.json
```

The service has one met, one partial and one unknown must-have. Its feedback claim remains unknown without reviewed evidence of an implemented change. Human work can meet a service requirement; it does not become a technology-autonomy score.

## Try a failure case

In a local copy of an example, change an offering's `revision` without updating its `reviewContext`. The comparison marks it stale and all findings Unknown. Change a success criterion and its previous finding also becomes Unknown.

Do not commit completed customer evaluations here. Use a private location for your own evidence and results.
