# Vegetation Browning Beyond Climatic Drought: Agro-Climatic Trend, Rainfall Decoupling and Land-Change Evidence in Northern Nigeria

## Overview

This project examines whether vegetation browning across Northern Nigeria can be interpreted as climatic drought alone. Instead of relying on state-level aggregation, the analysis uses agro-climatic zones based on **length of growing period (LGP)** to better follow the regional ecological and moisture gradient.

The workflow evaluates vegetation and rainfall trends from **2001–2025**, corrects statistical inference for serial correlation and multiple testing, identifies vegetation–rainfall decoupling, and tests whether independent land-cover and forest-loss evidence supports a non-climatic interpretation.

## Research Question

**Where does statistically robust vegetation decline occur without a corresponding decline in rainfall, and does independent land-change evidence support an interpretation beyond climatic drought alone?**

## Study Area

Northern Nigeria, represented through five occupied agro-climatic LGP strata:

- LGP <60 days
- LGP 60–119 days
- LGP 120–179 days
- LGP 180–239 days
- LGP 240–299 days

This ecological framework reduces reliance on administrative aggregation and addresses the **modifiable areal unit problem (MAUP)** that can distort state-level comparisons.

## Data and Analytical Framework

| Component | Role |
|---|---|
| NDVI | Primary vegetation-greenness indicator |
| EVI | Independent vegetation-index robustness check |
| Rainfall | Climatic trend / decoupling indicator |
| GAEZ LGP zones | Agro-climatic analytical geography |
| Dynamic World | Land-cover change evidence, 2016–2025 |
| Hansen forest loss | Independent forest-loss evidence, 2001–2025 |

## Statistical Method

Trend magnitude is estimated with **Sen/Theil–Sen slope**.

Serial correlation is addressed using **Hamed–Rao modified Mann–Kendall** inference. Where Hamed–Rao is mathematically undefined, **trend-free prewhitening (TFPW) modified Mann–Kendall** is used as a documented fallback.

Multiple hypothesis testing is controlled with the **Benjamini–Hochberg false discovery rate (FDR)** procedure.

## Key Findings

- The **LGP 180–239 day** zone is the principal rainfall-decoupled vegetation-decline regime.
- NDVI trend: **-0.002754 per year**, FDR-adjusted p = **0.000096**.
- EVI independently declines at **-0.001671 per year**, FDR-adjusted p = **0.000849**.
- Rainfall shows **no statistically significant decline** in the target zone; FDR-adjusted p = **0.682538**.
- Cropland changed by **+2.22 percentage points**.
- Tree cover changed by **-8.88 percentage points**.
- Forest loss reached **1,123.1 km²**, equivalent to **28.07%** of baseline forest.
- The integrated interpretation is retained in **77.8% of 81 robustness scenarios**.

## Interpretation

The final evidence does **not** support describing the target zone simply as a climatic drought hotspot.

Significant vegetation decline occurs despite statistically stable rainfall, while independent land-change evidence shows cropland expansion, tree-cover decline and substantial forest loss. The most defensible interpretation is therefore that the observed browning is **more consistent with land-use and vegetation-cover change than climatic drought alone**.

This is an **association-based interpretation, not causal proof**.

## Important Limitation

Conflict attribution is **deferred**. The conflict dataset available during reconstruction was restricted geographically and was not spatially representative of Northern Nigeria. Conflict is therefore not used as a definitive explanatory driver.

## Repository Structure

```text
assets/
  maps/
  charts/
data/
  final/
  tables/
docs/
reports/
```

The final validated package contains five scientific maps, six charts, authoritative result tables, final GIS data, and the technical report.

## Planning Relevance

The study shows why vegetation-index browning should not automatically be classified as drought. Environmental monitoring should jointly evaluate vegetation, rainfall and land-cover change so that drought-response measures are not substituted for land-management interventions where the evidence points to non-climatic pressures.

## Citation

Abdullah Abdazeez Ayomide. *Vegetation Browning Beyond Climatic Drought: Agro-Climatic Trend, Rainfall Decoupling and Land-Change Evidence in Northern Nigeria*. Geospatial environmental-planning project, 2026.
