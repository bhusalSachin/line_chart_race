import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from .utils import configure_plot

def create_animation(data_path, real_data_path, column_names, window_size=300):
    """Create an animated line chart race."""
    df = pd.read_csv(data_path)
    real_df = pd.read_csv(real_data_path)

    fig, ax, lines = configure_plot(df, column_names)

    def update(frame):
        if frame < window_size:
            start_year = df.index[0]
            end_year = df.index[frame]
        else:
            start_year = df.index[frame - window_size + 1]
            end_year = df.index[frame]

        ax.set_xlim(start_year, end_year)

        for region in column_names:
            x = df.index[(df.index >= start_year) & (df.index <= end_year)]
            y = df[region].loc[x]
            lines[region].set_data(x, y)

    ani = animation.FuncAnimation(fig, update, frames=len(df), init_func=lambda: None, blit=True)
    plt.show()

def save_animation(animation, file_path):
    """Save the generated animation."""
    animation.save(file_path, writer='ffmpeg')
