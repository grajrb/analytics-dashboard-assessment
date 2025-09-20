"""
Data exploration script for Electric_Vehicle_Population_Data.csv
Produces basic prints (head, info, describe, columns) and saves simple plots to outputs/.
"""
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_PATH = os.path.join(ROOT, 'data-to-visualize', 'Electric_Vehicle_Population_Data.csv')
OUTPUT_DIR = os.path.join(ROOT, 'outputs')

os.makedirs(OUTPUT_DIR, exist_ok=True)

def find_column(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    # try case-insensitive match
    lc = {col.lower(): col for col in df.columns}
    for c in candidates:
        if c.lower() in lc:
            return lc[c.lower()]
    return None


def main():
    if not os.path.exists(DATA_PATH):
        print(f"Data file not found at {DATA_PATH}")
        sys.exit(2)

    df = pd.read_csv(DATA_PATH)

    print('\n=== head() ===')
    print(df.head().to_string(index=False))

    print('\n=== info() ===')
    df.info(buf=sys.stdout)

    print('\n=== describe() ===')
    try:
        print(df.describe(include='all').to_string())
    except Exception:
        print(df.describe().to_string())

    print('\n=== columns ===')
    print(list(df.columns))

    # Try plotting Model Year distribution and Electric Range trend
    my_col = find_column(df, ['Model Year', 'Model_Year', 'model_year', 'ModelYear'])
    range_col = find_column(df, ['Electric Range', 'electric_range', 'ElectricRange', 'Electric Range (mi)'])

    if my_col is not None:
        try:
            counts = df[my_col].value_counts().sort_index()
            plt.figure(figsize=(10,6))
            counts.plot(kind='bar')
            plt.title('Count by Model Year')
            plt.xlabel(my_col)
            plt.ylabel('Count')
            plt.tight_layout()
            out = os.path.join(OUTPUT_DIR, 'count_by_model_year.png')
            plt.savefig(out)
            print(f"Saved plot: {out}")
            plt.close()
        except Exception as e:
            print('Could not create Model Year plot:', e)
    else:
        print('No Model Year column found for plotting')

    if my_col is not None and range_col is not None:
        try:
            agg = df.groupby(my_col)[range_col].mean().sort_index()
            plt.figure(figsize=(10,6))
            agg.plot(marker='o')
            plt.title('Average Electric Range by Model Year')
            plt.xlabel(my_col)
            plt.ylabel(range_col)
            plt.tight_layout()
            out = os.path.join(OUTPUT_DIR, 'avg_range_by_model_year.png')
            plt.savefig(out)
            print(f"Saved plot: {out}")
            plt.close()
        except Exception as e:
            print('Could not create Electric Range plot:', e)
    else:
        print('No Electric Range or Model Year column found for the second plot')

    print('\nDone.')

if __name__ == '__main__':
    main()
