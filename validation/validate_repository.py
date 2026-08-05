from pathlib import Path
import json
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md", "project.json", "LICENSE", "CITATION.cff", "requirements.txt",
    "assets/project-cover.png", "assets/repository-social-preview.png",
    "docs/DATA_SOURCES.md", "docs/METHODOLOGY.md", "docs/LIMITATIONS.md",
    "scripts/python/reproduce_summary.py",
    "data/processed/tables/regional_mann_kendall_sen_slope_trends_2001_2025.csv",
    "data/processed/tables/state_integrated_climate_vegetation_pressure_ranking.csv",
    "outputs/maps/01_integrated_climate_vegetation_pressure.png"
]
failures = [f"Missing: {p}" for p in required if not (ROOT / p).exists()]

for path in ROOT.rglob("*"):
    if path.is_file() and path.stat().st_size > 24 * 1024 * 1024:
        failures.append(f"Browser-upload limit exceeded: {path.relative_to(ROOT)}")

try:
    meta = json.loads((ROOT/"project.json").read_text(encoding="utf-8"))
    if meta["headline_results"]["most_extensive_compound_year"] != 2015:
        failures.append("Unexpected compound-stress year in metadata")
except Exception as exc:
    failures.append(f"Invalid metadata: {exc}")

try:
    trend = pd.read_csv(ROOT/"data/processed/tables/regional_mann_kendall_sen_slope_trends_2001_2025.csv")
    ndvi = trend.loc[trend["Variable"] == "Growing-season NDVI"].iloc[0]
    if abs(float(ndvi["Sen_Slope_per_Year"]) + 0.0007769114797049708) > 1e-12:
        failures.append("Regional NDVI slope mismatch")
except Exception as exc:
    failures.append(f"Could not validate trend results: {exc}")

if failures:
    print("REPOSITORY VALIDATION: FAILED")
    for f in failures:
        print("-", f)
    sys.exit(1)

print("REPOSITORY VALIDATION: PASSED")
print("Required files, upload-size limits and headline results are valid.")
