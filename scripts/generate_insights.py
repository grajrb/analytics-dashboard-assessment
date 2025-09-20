"""
Generate key insights and save charts/summary for the EV dataset.
Saves PNGs to ../outputs and a CSV summary.
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
    lc = {col.lower(): col for col in df.columns}
    for c in candidates:
        if c.lower() in lc:
            return lc[c.lower()]
    return None


def safe_save(fig, path):
    try:
        fig.savefig(path, bbox_inches='tight')
        print(f"Saved: {path}")
    except Exception as e:
        print(f"Failed saving {path}: {e}")


def main():
    if not os.path.exists(DATA_PATH):
        print(f"Data file not found at {DATA_PATH}")
        sys.exit(2)

    df = pd.read_csv(DATA_PATH)
    print('Loaded rows:', len(df))

    # identify columns
    year_col = find_column(df, ['Model Year', 'Model_Year', 'model_year'])
    county_col = find_column(df, ['County'])
    city_col = find_column(df, ['City'])
    make_col = find_column(df, ['Make'])
    model_col = find_column(df, ['Model'])
    evtype_col = find_column(df, ['Electric Vehicle Type', 'Electric_Vehicle_Type'])
    range_col = find_column(df, ['Electric Range', 'ElectricRange', 'electric_range'])
    cafv_col = find_column(df, ['Clean Alternative Fuel Vehicle (CAFV) Eligibility', 'CAFV Eligibility', 'CAFV'])

    summaries = {}

    # Growth Over Time: count by model year
    if year_col:
        growth = df[year_col].value_counts().sort_index()
        fig, ax = plt.subplots(figsize=(10,6))
        growth.plot(ax=ax)
        ax.set_title('EV count by Model Year')
        ax.set_xlabel(year_col)
        ax.set_ylabel('Count')
        safe_save(fig, os.path.join(OUTPUT_DIR, 'growth_by_model_year.png'))
        plt.close(fig)
        summaries['growth_by_model_year'] = growth
    else:
        print('Model Year column not found; skipping growth over time')

    # Geographical distribution: top 10 counties and cities
    if county_col:
        top_counties = df[county_col].value_counts().head(10)
        fig, ax = plt.subplots(figsize=(10,6))
        top_counties.plot(kind='bar', ax=ax)
        ax.set_title('Top 10 Counties by EV count')
        ax.set_xlabel('County')
        ax.set_ylabel('Count')
        safe_save(fig, os.path.join(OUTPUT_DIR, 'top10_counties.png'))
        plt.close(fig)
        summaries['top_counties'] = top_counties
    else:
        print('County column not found')

    if city_col:
        top_cities = df[city_col].value_counts().head(10)
        fig, ax = plt.subplots(figsize=(10,6))
        top_cities.plot(kind='bar', ax=ax)
        ax.set_title('Top 10 Cities by EV count')
        ax.set_xlabel('City')
        ax.set_ylabel('Count')
        safe_save(fig, os.path.join(OUTPUT_DIR, 'top10_cities.png'))
        plt.close(fig)
        summaries['top_cities'] = top_cities
    else:
        print('City column not found')

    # Vehicle popularity: top makes and models (horizontal bar)
    if make_col:
        top_makes = df[make_col].value_counts().head(10)
        fig, ax = plt.subplots(figsize=(8,6))
        top_makes.plot(kind='barh', ax=ax)
        ax.invert_yaxis()
        ax.set_title('Top 10 Makes')
        ax.set_xlabel('Count')
        safe_save(fig, os.path.join(OUTPUT_DIR, 'top10_makes.png'))
        plt.close(fig)
        summaries['top_makes'] = top_makes
    else:
        print('Make column not found')

    if model_col:
        top_models = df[model_col].value_counts().head(10)
        fig, ax = plt.subplots(figsize=(8,6))
        top_models.plot(kind='barh', ax=ax)
        ax.invert_yaxis()
        ax.set_title('Top 10 Models')
        ax.set_xlabel('Count')
        safe_save(fig, os.path.join(OUTPUT_DIR, 'top10_models.png'))
        plt.close(fig)
        summaries['top_models'] = top_models
    else:
        print('Model column not found')

    # EV Types distribution
    if evtype_col:
        ev_types = df[evtype_col].value_counts()
        fig, ax = plt.subplots(figsize=(6,6))
        ev_types.plot(kind='pie', autopct='%1.1f%%', ax=ax)
        ax.set_ylabel('')
        ax.set_title('EV Type Distribution')
        safe_save(fig, os.path.join(OUTPUT_DIR, 'ev_type_distribution.png'))
        plt.close(fig)
        summaries['ev_types'] = ev_types
    else:
        print('Electric Vehicle Type column not found')

    # Electric Range by Model Year (average)
    if year_col and range_col:
        try:
            df[range_col] = pd.to_numeric(df[range_col], errors='coerce')
            avg_range = df.groupby(year_col)[range_col].mean().dropna().sort_index()
            fig, ax = plt.subplots(figsize=(10,6))
            avg_range.plot(marker='o', ax=ax)
            ax.set_title('Average Electric Range by Model Year')
            ax.set_xlabel(year_col)
            ax.set_ylabel(range_col)
            safe_save(fig, os.path.join(OUTPUT_DIR, 'avg_range_by_model_year.png'))
            plt.close(fig)
            summaries['avg_range_by_model_year'] = avg_range
        except Exception as e:
            print('Error computing avg range by year:', e)
    else:
        print('Model Year or Electric Range column missing; skipping electric range analysis')

    # CAFV eligibility counts
    if cafv_col:
        cafv_counts = df[cafv_col].value_counts()
        fig, ax = plt.subplots(figsize=(6,6))
        cafv_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax)
        ax.set_ylabel('')
        ax.set_title('CAFV Eligibility')
        safe_save(fig, os.path.join(OUTPUT_DIR, 'cafv_eligibility.png'))
        plt.close(fig)
        summaries['cafv'] = cafv_counts
    else:
        print('CAFV column not found')

    # Save numeric summaries to CSV
    summary_csv = os.path.join(OUTPUT_DIR, 'insights_summary.csv')
    try:
        rows = []
        # growth
        if 'growth_by_model_year' in summaries:
            s = summaries['growth_by_model_year']
            df_growth = s.rename_axis(year_col).reset_index(name='count')
            df_growth.to_csv(os.path.join(OUTPUT_DIR, 'growth_by_model_year.csv'), index=False)
        if 'avg_range_by_model_year' in summaries:
            summaries['avg_range_by_model_year'].rename_axis(year_col).reset_index(name='avg_electric_range').to_csv(os.path.join(OUTPUT_DIR, 'avg_range_by_model_year.csv'), index=False)
        if 'top_makes' in summaries:
            summaries['top_makes'].rename_axis('Make').reset_index(name='count').to_csv(os.path.join(OUTPUT_DIR, 'top10_makes.csv'), index=False)
        if 'top_models' in summaries:
            summaries['top_models'].rename_axis('Model').reset_index(name='count').to_csv(os.path.join(OUTPUT_DIR, 'top10_models.csv'), index=False)
        if 'top_cities' in summaries:
            summaries['top_cities'].rename_axis('City').reset_index(name='count').to_csv(os.path.join(OUTPUT_DIR, 'top10_cities.csv'), index=False)
        if 'top_counties' in summaries:
            summaries['top_counties'].rename_axis('County').reset_index(name='count').to_csv(os.path.join(OUTPUT_DIR, 'top10_counties.csv'), index=False)
        if 'ev_types' in summaries:
            summaries['ev_types'].rename_axis('EV Type').reset_index(name='count').to_csv(os.path.join(OUTPUT_DIR, 'ev_type_distribution.csv'), index=False)
        if 'cafv' in summaries:
            summaries['cafv'].rename_axis('CAFV Eligibility').reset_index(name='count').to_csv(os.path.join(OUTPUT_DIR, 'cafv_counts.csv'), index=False)

        print('Saved CSV summaries to outputs/')
    except Exception as e:
        print('Failed to save CSV summaries:', e)

    print('\nDone generating insights.')

if __name__ == '__main__':
    main()
