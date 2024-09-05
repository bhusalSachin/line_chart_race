from .data_processing import prepare_data
from .plot_animation import create_animation, save_animation
from .config import config
from .interpolation import interpolate_data

def run_chart_race():
    interp_data = interpolate_data(config('real_data_path'))
    # df = prepare_data(config['data_path'], config['interval'])
    df = prepare_data(interp_data, config['interval'])
    create_animation(df, config['real_data_path'], config['columns'])
    save_animation(df, config['output_path'])