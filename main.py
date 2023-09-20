"""
Main cli or app entry point
"""

# from mylib.calculator import add
# import click

#import pandas as pd
import matplotlib.pyplot as plt
from mylib.lib import (read_file,  Rating_plot, MetaScore_plot)
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

# @click.command("add")
# @click.argument("a", type=int)
# @click.argument("b", type=int)
# def add_cli(a, b):
#     click.echo(add(a, b))


# if __name__ == "__main__":
#     # pylint: disable=no-value-for-parameter

