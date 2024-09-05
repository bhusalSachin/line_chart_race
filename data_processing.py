import pandas as pd
import numpy as np

def add_granular_years(df, start_year, end_year, interval=0.1):
    """Add interpolated granular years to the DataFrame."""
    years = np.arange(start_year, end_year + interval, interval)
    granular_years = pd.DataFrame(years, columns=['Year'])
    df = pd.merge(granular_years, df, on='Year', how='left')
    df.set_index('Year', inplace=True)
    df.interpolate(method='linear', inplace=True)
    df.reset_index(inplace=True)
    return df

def interpolate_data(df, num_points=3000):
    """Interpolate data for smoother animation."""
    interp_df = pd.DataFrame()
    x_interp = np.linspace(df.index.min(), df.index.max(), num_points)
    for col in df.columns:
        y_interp = np.interp(x_interp, df.index, df[col])
        interp_df[col] = y_interp
    interp_df.index = x_interp
    return interp_df

def prepare_data(data_path, interval=0.1):
    """Main function to prepare data with interpolation and save the processed file."""
    # df = pd.read_csv(data_path
    df = data_path
    df = add_granular_years(df, df['Year'].min(), df['Year'].max(), interval)
    df_filtered_interp = interpolate_data(df.set_index('Year'))
    return df_filtered_interp
