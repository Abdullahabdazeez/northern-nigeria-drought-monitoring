# Project Report: Vegetation Browning Beyond Climatic Drought in Northern Nigeria

## Background

Vegetation browning is often treated as a sign of drought, but that explanation can be misleading when rainfall is not actually declining.

I built this project to separate those two ideas. The aim was to find places in Northern Nigeria where vegetation shows a clear long-term decline, then check whether rainfall shows the same trend. Where the two do not move together, I bring in independent land-cover and forest-loss evidence before deciding what the pattern may mean.

## What I did

I analysed vegetation and rainfall trends from **2001 to 2025**. Instead of grouping the results only by state boundaries, I used agro-climatic zones based on **length of growing period (LGP)** so that the analysis followed the regional ecological gradient more closely.

Trend size was estimated with Sen/Theil-Sen slope. I corrected the significance testing for serial correlation and controlled repeated testing with the Benjamini-Hochberg false discovery rate procedure.

I then compared the vegetation-rainfall pattern with Dynamic World land-cover change and Hansen forest-loss evidence.

## What I found

The clearest case appears in the **LGP 180-239 day zone**.

NDVI declines at **-0.002754 per year** and EVI declines at **-0.001671 per year**. Both trends remain statistically significant after false-discovery-rate adjustment.

Rainfall, however, does not show a statistically significant decline in the same zone. Its adjusted p-value is **0.682538**.

Independent land-change evidence also shows:

- cropland increasing by **2.22 percentage points**;
- tree cover declining by **8.88 percentage points**; and
- **1,123.1 km²** of forest loss, equal to **28.07%** of baseline forest in the analysed target area.

The integrated interpretation is retained in **77.8% of 81 robustness scenarios**.

## What the result means

The evidence does not support calling the target zone a simple climatic-drought hotspot.

Vegetation is declining, but rainfall is not declining in the same way. At the same time, the independent land-change evidence points toward cropland expansion, tree-cover loss and substantial forest loss.

The most cautious interpretation is therefore that the browning is **more consistent with land-use and vegetation-cover change than with climatic drought alone**.

That is still an association-based interpretation. It does not prove one single cause.

## Why the statistical corrections matter

Environmental time series are often serially correlated, which can make ordinary trend tests look more significant than they really are. Repeated testing across several zones also increases the chance of finding a false positive by accident.

Correcting for both issues made the analysis more conservative, but also made the final result easier to defend.

## What I did not claim

I did not make a final conflict-attribution claim. The conflict dataset available during reconstruction was geographically restricted and was not representative enough of Northern Nigeria to support that conclusion.

Leaving that claim out is preferable to forcing a story that the data cannot support.

## What I would add next

A stronger next step would use a more complete land-use history and locally representative conflict, grazing, agricultural-intensity or fire data. Field or high-resolution imagery checks in the target zone would also help distinguish different forms of vegetation loss.

## Main outputs

Final maps are in [`assets/maps`](../assets/maps/), charts in [`assets/charts`](../assets/charts/), data tables in [`data`](../data/) and the technical material is in [`reports`](../reports/).

## Final note

The main lesson from this project is simple: a falling vegetation index should not automatically be called drought. The climate signal and the land-change signal need to be checked separately before they are interpreted together.
