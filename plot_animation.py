import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from .utils import configure_plot

def create_animation(df, window_size=300):
    """Create an animated line chart race using DataFrame directly."""
    # Assuming df is already a DataFrame, no need to read it again
    column_names = df.columns.tolist()

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
    # ani.save('line_chart_race.mp4', writer='ffmpeg', fps=30)
    plt.show()

def save_animation(animation, file_path):
    """Save the generated animation."""
    animation.save(file_path, writer='ffmpeg')
