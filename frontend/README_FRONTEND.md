# Frontend (Next.js) — EV Dashboard

This folder contains a minimal Next.js app that renders charts using the CSV summaries generated in `outputs/`.

Install and run locally (Windows/cmd.exe):

1. From repository root, change to frontend:

```cmd
cd frontend
```

2. Install dependencies:

```cmd
npm install
```

3. Run dev server:

```cmd
npm run dev
```

4. Open http://localhost:3000

Notes:
- The Next.js API route reads CSV files from the repo `outputs/` folder (e.g. `outputs/growth_by_model_year.csv`). Ensure you have generated them using `scripts/generate_insights.py`.
- If you prefer to serve static files from `public/`, copy CSVs from `outputs/` into `frontend/public/data/` and update the client fetch paths accordingly.
