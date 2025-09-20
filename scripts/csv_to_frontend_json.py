"""
Convert the dataset CSV to a JSON file for the Next.js frontend public folder.
Writes to frontend/public/ev_data.json (creates the folder if needed).
"""
import os
import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CSV_PATH = os.path.join(ROOT, 'data-to-visualize', 'Electric_Vehicle_Population_Data.csv')
OUT_DIR = os.path.join(ROOT, 'frontend', 'public')
OUT_PATH = os.path.join(OUT_DIR, 'ev_data.json')

os.makedirs(OUT_DIR, exist_ok=True)

if not os.path.exists(CSV_PATH):
    print('CSV not found at', CSV_PATH)
    raise SystemExit(1)

print('Reading', CSV_PATH)
df = pd.read_csv(CSV_PATH)
print('Rows:', len(df))

# Convert to records orientation; ensure serializable types
json_str = df.to_json(orient='records', date_format='iso')
with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write(json_str)

print('Wrote', OUT_PATH)
