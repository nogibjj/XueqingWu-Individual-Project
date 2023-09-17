"""
Main cli or app entry point
"""

# from mylib.calculator import add
# import click

import polars as pl
import matplotlib.pyplot as plt
""""Import packages"""

#var=1;var=2

def read_file(file_name):
    # create the data summary
    df = pl.read_csv(file_name, ignore_errors=True)
    # print(df.head())
    return df

def summary(file_name):
    df=read_file(file_name)
    print(df.describe())
    return df.describe()

def summary_plot(file_name):
    df=read_file(file_name)
    plt.hist(df['IMDB_Rating'])
    plt.show()

# @click.command("add")
# @click.argument("a", type=int)
# @click.argument("b", type=int)
# def add_cli(a, b):
#     click.echo(add(a, b))


# if __name__ == "__main__":
#     # pylint: disable=no-value-for-parameter

