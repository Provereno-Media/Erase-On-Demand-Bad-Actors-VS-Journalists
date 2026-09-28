#!/usr/bin/env python3
"""Integrity checks for the Erase on Demand dataset (stdlib only)."""
import csv, json, re, sys, pathlib
D = pathlib.Path(__file__).resolve().parent.parent / "data"
err = []
def load(n): return list(csv.DictReader(open(D / f"{n}.csv", encoding="utf-8")))
cases, sources, actors, comp = (load(n) for n in ("cases", "sources", "actors", "comparative_cases"))
def uniq(rows, key, name):
    ids = [r[key] for r in rows]
    for d in {i for i in ids if ids.count(i) > 1}: err.append(f"{name}: duplicate {key} {d}")
    return set(ids)
src_ids = uniq(sources, "source_id", "sources")
uniq(cases, "case_id", "cases"); uniq(actors, "actor_id", "actors"); uniq(comp, list(comp[0])[0], "comparative")
for c in cases:
    for s in re.split(r"[;,]\s*", c.get("source_ids", "")):
        if s and s.startswith("SRC") and s not in src_ids: err.append(f"{c['case_id']}: unknown source {s}")
    if c["confidence"] not in ("Confirmed", "Unverified", "Plausible"): err.append(f"{c['case_id']}: bad confidence {c['confidence']}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", c.get("last_verified", "")): err.append(f"{c['case_id']}: bad last_verified")
pkg = json.load(open(D / "datapackage.json"))
for r in pkg["resources"]:
    n = r["name"]; hdr = next(csv.reader(open(D / f"{n}.csv", encoding="utf-8")))
    fields = [f["name"] for f in r.get("schema", {}).get("fields", [])]
    if fields and fields != hdr: err.append(f"{n}: header != datapackage schema")
print(f"cases={len(cases)} sources={len(sources)} actors={len(actors)} comparative={len(comp)}")
for e in err: print("ERROR", e)
sys.exit(1 if err else 0)
