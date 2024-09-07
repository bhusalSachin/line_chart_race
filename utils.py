config = {
    'data_path': './data.csv',
    'real_data_path': './real_data.csv',
    'columns': ['Urban Population', 'Rural Population'],
    'output_path': './line_chart_race.mp4',
    'interval': 0.5,
    'num_points': 3000,
}

import matplotlib.pyplot as plt

def configure_plot(df, column_names):
    """Set up the plot, initialize lines for each column, and remove the borders."""
    fig, ax = plt.subplots()
    
    # Create a line for each column
    lines = {}
    for col in column_names:
        lines[col], = ax.plot([], [], label=col)

    # Set up plot appearance
    ax.set_xlim(df.index.min(), df.index.max())
    ax.set_ylim(df.min().min(), df.max().max())
    ax.legend(loc='upper left')

    # Remove borders (spines)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    return fig, ax, lines
