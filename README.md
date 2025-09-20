# MapUp - Analytics Dashboard Assessment (Consolidated)

## Live Dashboard

Deployed URL: [https://analytics-dashboard-assessment-beta-six.vercel.app/](https://analytics-dashboard-assessment-beta-six.vercel.app/)

## Overview

This repository contains an end-to-end analytics dashboard for an Electric Vehicle (EV) population dataset. It includes Python scripts for data exploration and summary generation, plus a Next.js frontend (in `frontend/`) that renders charts using Recharts and Tailwind CSS.

### Key pieces

- Data: `data-to-visualize/Electric_Vehicle_Population_Data.csv`
- Data processing scripts: `scripts/` (exploration, insights, CSV→JSON conversion)
- Generated outputs: `outputs/` (PNGs and CSV summaries)
- Frontend: `frontend/` (Next.js app)

## How to run locally

1. Create & activate a Python virtual environment (optional but recommended):

```cmd
python -m venv .venv
.venv\Scripts\activate
```

1. Install Python dependencies and run data scripts:

```cmd
pip install -r requirements.txt
python scripts/data_exploration.py
python scripts/generate_insights.py
```

1. Generate the frontend JSON snapshot (optional):

```cmd
.venv\Scripts\python.exe scripts/csv_to_frontend_json.py
```

1. Run the frontend (from repo root):

```cmd
cd frontend
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

## Deploying to Vercel

The project has been deployed to Vercel: [https://analytics-dashboard-assessment-beta-six.vercel.app/](https://analytics-dashboard-assessment-beta-six.vercel.app/)

If you want to re-deploy from your account, import the repository in Vercel and set the Root Directory to `frontend`.

## Collaborators (evaluation access)

Please keep the repository private and add the following emails as collaborators so our evaluators can access the submission:

If you need to add collaborators on GitHub, add these evaluator emails (recommended to keep the repo private):

- `vedantp@mapup.ai`
- `ajayap@mapup.ai`
- `atharvd@mapup.ai`

## Notes & Recommendations

- The frontend currently reads a static JSON snapshot at `frontend/public/ev_data.json`. For production, prefer shipping smaller summary CSVs under `frontend/public/data/` 

## Files of interest

- `scripts/data_exploration.py` — initial exploration and plots
- `scripts/generate_insights.py` — saves PNGs and CSV summaries to `outputs/`
- `scripts/csv_to_frontend_json.py` — writes `frontend/public/ev_data.json`
- `frontend/pages/index.js` — main dashboard page
