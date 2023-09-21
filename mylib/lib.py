"""
Main cli or app entry point
"""

# from mylib.calculator import add
# import click

import pandas as pd
import matplotlib.pyplot as plt
""""Import packages"""

#var=1;var=2

def read_file(file_name):
    # create the data summary
    df = pd.read_csv(file_name)
    # print(df.head())
    return df

def summary(file_name):
    df=read_file(file_name)
    # print(df.describe())
    return df.describe()

def Rating_plot(file_name):
    df=read_file(file_name)
    plt.hist(df['IMDB_Rating'])
    plt.show()

def MetaScore_plot(file_name):
    df=read_file(file_name)
    plt.hist(df['Meta_score'])
    plt.show() 


def Rating_plot_save(file_name):
    df=read_file(file_name)
    plt.hist(df['IMDB_Rating'])
    plt.savefig('Rating_plot.png') 

def MetaScore_plot_save(file_name):
    df=read_file(file_name)
    plt.hist(df['Meta_score'])
    plt.savefig('MetaScore_plot.png') 

# @click.command("add")
# @click.argument("a", type=int)
# @click.argument("b", type=int)
# def add_cli(a, b):
#     click.echo(add(a, b))


# if __name__ == "__main__":
#     # pylint: disable=no-value-for-parameter

