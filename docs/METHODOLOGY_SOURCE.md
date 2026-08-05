# Methodology

## 1. Study Area

The study covers 19 states across Northern Nigeria:

- North West: Jigawa, Kaduna, Kano, Katsina, Kebbi, Sokoto and Zamfara.
- North East: Adamawa, Bauchi, Borno, Gombe, Taraba and Yobe.
- North Central: Benue, Kogi, Kwara, Nasarawa, Niger and Plateau.

## 2. Vegetation Analysis

MODIS MOD13Q1 V6.1 16-day NDVI and EVI data were processed for 2001–2025.

SummaryQA values of 0 and 1 were retained.

The MODIS scale factor of 0.0001 was applied.

Monthly composites were generated, followed by annual and May–October growing-season composites.

## 3. Rainfall Analysis

CHIRPS Daily precipitation was aggregated to monthly, annual and May–October totals.

The 1981–2025 period was used as the rainfall climatological baseline.

## 4. Drought Analysis

Rainfall anomalies were standardized against the long-term climatology.

SPI-3 and SPI-6 were calculated from monthly CHIRPS precipitation.

Drought conditions were identified when SPI <= -1.

## 5. Vegetation Stress

NDVI and EVI anomalies were standardized relative to each area's 2001–2025 distribution.

Vegetation stress was defined primarily using NDVI z-scores.

Vegetation Condition Index was calculated relative to the observed minimum and maximum NDVI.

## 6. Trend Analysis

Mann–Kendall tests were applied to detect monotonic trends.

Sen's slope was used to estimate trend magnitude.

Statistical significance was evaluated at alpha = 0.05.

## 7. Compound Hotspots

State-year SPI-6 drought conditions were matched temporally with vegetation-stress years.

Long-term drought frequency, vegetation stress and concurrence were integrated into a relative compound hotspot score.

## 8. Integrated Pressure

The final pressure score combined:

- vegetation browning;
- temperature trend;
- SPI-6 drought frequency;
- compound drought–vegetation stress.

The resulting score is a relative planning-priority diagnostic.

## 9. Validation

Validation was performed after every major stage using:

- record counts;
- temporal completeness;
- spatial coverage;
- missing-value checks;
- geometry validity;
- expected state/year totals;
- independent file re-opening;
- statistical consistency checks;
- visual inspection of maps and charts.