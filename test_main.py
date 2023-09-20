"""
Test goes here

"""

# from mylib.calculator import add


# def test_add():
#     assert add(1, 2) == 3

from main import summary, summary_plot
#import matplotlib.pyplot as plt
#import polars as pl

"Test the dataset summary"


# def test_read_file():
#     df=read_file('imdb_top_1000.csv')
#     # assert not df.empty()
#     assert len(df)==1000

def test_describe():
    # describe=read_file('imdb_top_1000.csv')
    # assert describe['IMDB_Rating'].mean()==7.949299999999999
    # assert describe['IMDB_Rating'].max()==9.3
    describe=summary('imdb_top_1000.csv')
    assert describe.loc["mean", "IMDB_Rating"]==7.949299999999999
    assert describe.loc["max", "IMDB_Rating"]==9.3

def test_graph():
    # df=read_file('imdb_top_1000.csv')
    # plt.hist(df['IMDB_Rating'])
    # plt.show()
    summary_plot('imdb_top_1000.csv')



if __name__ == "__main__":
    #test_read_file()
    test_describe()
    test_graph()
