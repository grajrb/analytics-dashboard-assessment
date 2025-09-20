# Data Exploration — how to run

This folder contains a small script to explore the provided EV dataset and produce basic plots.

Run these steps in Windows `cmd.exe` from the repository root:

1. Create & activate a virtual environment (optional but recommended):

python -m venv .venv
.venv\Scripts\activate

2. Install dependencies:

pip install -r requirements.txt

3. Run the exploration script:

python scripts\data_exploration.py

Outputs (PNG files) will be saved to an `outputs/` directory at the repository root.
