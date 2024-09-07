from .data_processing import prepare_data
from .plot_animation import create_animation, save_animation
from .config import config
from .interpolation import interpolate_data

def run_chart_race():
    interp_data = interpolate_data(config['real_data_path'])
    # Directly pass the interpolated data to `prepare_data`
    df = prepare_data(interp_data, config['interval'])
    
    # Pass the DataFrame directly to create_animation
    create_animation(df)
    
    save_animation(df, config['output_path'])
