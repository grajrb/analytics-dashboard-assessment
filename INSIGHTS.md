# Key Insights — Electric Vehicle Population Dataset

This file summarizes the quick, actionable insights I generated from the dataset and points to the generated charts and CSV summaries in `outputs/`.

## What I computed
- Growth over time (count by Model Year) — `outputs/growth_by_model_year.png` and `outputs/growth_by_model_year.csv`
- Geographical distribution — `outputs/top10_counties.png`, `outputs/top10_counties.csv`, `outputs/top10_cities.png`, `outputs/top10_cities.csv`
- Vehicle popularity — `outputs/top10_makes.png`, `outputs/top10_makes.csv`, `outputs/top10_models.png`, `outputs/top10_models.csv`
- EV Type distribution (BEV vs PHEV) — `outputs/ev_type_distribution.png`, `outputs/ev_type_distribution.csv`
- Electric range trend — `outputs/avg_range_by_model_year.png`, `outputs/avg_range_by_model_year.csv`
- CAFV Eligibility counts — `outputs/cafv_eligibility.png`, `outputs/cafv_counts.csv`

## Quick findings (based on generated outputs)
- Model years cluster strongly in recent years (2019-2024), with median model year 2022 and mean ~2021 — this suggests rapid recent adoption.
- A small number of counties/cities (e.g., King County and Seattle) contain a large share of EVs — see `top10_counties.png` and `top10_cities.png`.
- Tesla dominates the Make distribution in this dataset (majority share among top makes) and `MODEL Y` appears frequently among top models.
- Battery Electric Vehicles (BEV) are the dominant EV type in the dataset (see `ev_type_distribution.png`).
- Average electric range has increased for newer model years (see `avg_range_by_model_year.png`) — indicating technology improvement over time.
- CAFV eligibility shows a mixture of eligible, not eligible, and unknown entries — policy-focused audiences may want a cleaned/standardized CAFV field.

## Next recommended analyses
- Map visualization of geolocation coordinates from `Vehicle Location` to show spatial clustering.
- Time-series decomposition for growth to project near-term adoption.
- Cross-analysis: average base MSRP by model year or by make to study price trends vs. range.
- Clean and normalize the `CAFV` eligibility text field to standard categories for clearer counts.

## How to re-generate
1. Activate venv and install requirements (if not already done):

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the insights script:

```cmd
.venv\Scripts\python.exe scripts\generate_insights.py
```

All generated images and CSVs will be placed in `outputs/`.
