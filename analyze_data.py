import pandas as pd
import numpy as np

# Load data to understand structure
gen_data = pd.read_csv('Datasets/Processed Datasets/Plant1_filtered.csv')
weather_data = pd.read_csv('Datasets/Processed Datasets/Plant1_Weather_filtered.csv')

print('Generation Data Info:')
print(f'Shape: {gen_data.shape}')
print(f'Date range: {gen_data["DATE_TIME"].min()} to {gen_data["DATE_TIME"].max()}')
print(f'Unique inverters: {gen_data["SOURCE_KEY"].nunique()}')
print(f'AC_POWER range: {gen_data["AC_POWER"].min():.2f} to {gen_data["AC_POWER"].max():.2f}')

print('\nWeather Data Info:')
print(f'Shape: {weather_data.shape}')
print(f'Date range: {weather_data["DATE_TIME"].min()} to {weather_data["DATE_TIME"].max()}')
print(f'Irradiation range: {weather_data["IRRADIATION"].min():.4f} to {weather_data["IRRADIATION"].max():.4f}')

# Check temporal frequency
gen_data['DATE_TIME'] = pd.to_datetime(gen_data['DATE_TIME'], format='mixed')
weather_data['DATE_TIME'] = pd.to_datetime(weather_data['DATE_TIME'])

gen_times = gen_data['DATE_TIME'].drop_duplicates().sort_values()
weather_times = weather_data['DATE_TIME'].drop_duplicates().sort_values()

print(f'\nGeneration data frequency (first 10 intervals):')
print(gen_times.head(10))

print(f'\nTime differences (minutes):')
time_diffs = gen_times.diff().dt.total_seconds() / 60
print(f'Generation data interval: {time_diffs.mode().iloc[0]:.1f} minutes')

weather_diffs = weather_times.diff().dt.total_seconds() / 60
print(f'Weather data interval: {weather_diffs.mode().iloc[0]:.1f} minutes')

# Aggregate generation data
gen_agg = gen_data.groupby('DATE_TIME')['AC_POWER'].sum().reset_index()
gen_agg.columns = ['DATE_TIME', 'total_AC_POWER']
print(f'\nAggregated AC_POWER range: {gen_agg["total_AC_POWER"].min():.2f} to {gen_agg["total_AC_POWER"].max():.2f}')
print(f'Total time points: {len(gen_agg)}')
