# Frontend (Next.js) — EV Dashboard

This folder contains a minimal Next.js app that renders charts from a JSON snapshot of the dataset placed in `frontend/public/ev_data.json`.

Install and run locally (Windows/cmd.exe):

1. From repository root, change to frontend:

```cmd
cd frontend
```

2. Install dependencies (npm):

```cmd
npm install
```

Or with bun (if installed):

```cmd
bun install
```

3. Run dev server:

```cmd
npm run dev
```

4. Open http://localhost:3000

Generating `ev_data.json`:

From the repository root you can generate a JSON snapshot of the whole CSV dataset that the frontend will read:

```cmd
.venv\Scripts\activate
.venv\Scripts\python.exe scripts\csv_to_frontend_json.py
```
