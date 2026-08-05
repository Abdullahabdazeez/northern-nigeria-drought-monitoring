from pathlib import Path
import pandas as pd
import math

ROOT = Path(__file__).resolve().parents[2]
TABLES = ROOT / "data" / "processed" / "tables"

regional = pd.read_csv(TABLES / "regional_mann_kendall_sen_slope_trends_2001_2025.csv")
regional = regional.set_index("Variable")

checks = {
    "Growing-season NDVI": (-0.0007769114797049708, 0.008520236731434604),
    "Growing-season EVI": (-0.0003578185827754629, 0.04125951957926039),
    "May–October rainfall": (2.5023371058301715, 0.20115677879053945),
    "May–October temperature": (0.015435023799214877, 0.02876822528460094),
}

for variable, (slope, pvalue) in checks.items():
    row = regional.loc[variable]
    if not math.isclose(float(row["Sen_Slope_per_Year"]), slope, rel_tol=0, abs_tol=1e-12):
        raise ValueError(f"Unexpected slope for {variable}")
    if not math.isclose(float(row["P_Value"]), pvalue, rel_tol=0, abs_tol=1e-12):
        raise ValueError(f"Unexpected p-value for {variable}")

pressure = pd.read_csv(TABLES / "state_integrated_climate_vegetation_pressure_ranking.csv")
compound = pd.read_csv(TABLES / "state_compound_drought_vegetation_hotspot_ranking.csv")

if pressure.iloc[0]["State"] != "Nasarawa":
    raise ValueError("Unexpected highest integrated-pressure state")
if compound.iloc[0]["State"] != "Kaduna":
    raise ValueError("Unexpected highest compound-hotspot state")

print("RESULT REPRODUCTION: PASSED")
print(f"Regional NDVI Sen slope: {checks['Growing-season NDVI'][0]:.6f}/year")
print(f"Regional temperature Sen slope: {checks['May–October temperature'][0]:.4f} °C/year")
print(f"Highest integrated pressure: {pressure.iloc[0]['State']} ({pressure.iloc[0]['Integrated_Pressure_Score']:.2f})")
print(f"Highest compound hotspot: {compound.iloc[0]['State']} ({compound.iloc[0]['Compound_Hotspot_Score']:.2f})")
