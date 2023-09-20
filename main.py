"""
Main cli or app entry point
"""

# from mylib.calculator import add
# import click

#import pandas as pd
import matplotlib.pyplot as plt
from mylib.lib import (read_file,  Rating_plot, MetaScore_plot, Rating_plot_save, MetaScore_plot_save)
""""Import packages"""

#var=1;var=2


def summary(file_name):
    df=read_file(file_name)
    print(df.describe())
    return df.describe()

def summary_plot(file_name):
    plt.subplot(2, 1, 1)
    Rating_plot(file_name)

    plt.subplot(2, 1, 2)
    MetaScore_plot(file_name)



def save_to_markdown(file_name):
    """save summary report to markdown"""
    describe_df = summary(file_name)
    markdown_table1 = describe_df.to_markdown()
    Rating_plot_save(file_name)
    MetaScore_plot_save(file_name)
    # Write the markdown table to a file
    with open("imdb_movie_summary.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("![Rating_plot](Rating_plot.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![MetaScore_plot](MetaScore_plot.png)\n")


# @click.command("add")
# @click.argument("a", type=int)
# @click.argument("b", type=int)
# def add_cli(a, b):
#     click.echo(add(a, b))


if __name__ == "__main__":
    save_to_markdown('imdb_top_1000.csv')

