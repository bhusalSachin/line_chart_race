import pandas as pd
import numpy as np

def interpolate_data(file_path, num_points=10):
    """
    Interpolates the data between known points for two unspecified columns read from a CSV file.

    Parameters:
    file_path (str): Path to the CSV file containing the data.
    num_points (int): Number of points to interpolate between each known point.

    Returns:
    pd.DataFrame: DataFrame with interpolated values.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Automatically detect the first two data columns (excluding 'Year')
    columns = df.columns.tolist()
    if 'Year' not in columns:
        raise ValueError("The CSV file must contain a 'Year' column.")
    
    # Ensure there are at least two other columns for interpolation
    data_columns = [col for col in columns if col != 'Year']
    if len(data_columns) < 2:
        raise ValueError("The CSV file must contain at least two data columns other than 'Year'.")
    
    col1, col2 = data_columns[0], data_columns[1]
    
    # Sort the DataFrame by the 'Year' column to ensure proper interpolation order
    df = df.sort_values('Year')



    # Create a new DataFrame to store interpolated results
    interpolated_data = pd.DataFrame(columns=['Year', col1, col2])

    # Interpolating between consecutive points
    for i in range(len(df) - 1):
        start_row = df.iloc[i]
        end_row = df.iloc[i + 1]

        # Interpolating between two years for both columns
        years = np.linspace(start_row['Year'], end_row['Year'], num=num_points)
        col1_values = np.linspace(start_row[col1], end_row[col1], num=num_points)
        col2_values = np.linspace(start_row[col2], end_row[col2], num=num_points)

        # Creating a DataFrame for the interpolated points
        temp_df = pd.DataFrame({
            'Year': years,
            col1: col1_values,
            col2: col2_values
        })

        # Appending the interpolated points to the main DataFrame
        if not temp_df.empty:
            interpolated_data = pd.concat([interpolated_data, temp_df])
        # interpolated_data = pd.concat([interpolated_data, temp_df])

    # Reset the index of the resulting DataFrame
    interpolated_data = interpolated_data.reset_index(drop=True)

    return interpolated_data

# Example usage:
# interpolated_df = interpolate_data('real_data_path.csv')
