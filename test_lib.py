from mylib.lib import read_file, summary, Rating_plot, MetaScore_plot


def test_read_file():
    df = read_file("imdb_top_1000.csv")
    # assert not df.empty()
    assert len(df) == 1000


def test_describe():
    # describe=read_file('imdb_top_1000.csv')
    # assert describe['IMDB_Rating'].mean()==7.949299999999999
    # assert describe['IMDB_Rating'].max()==9.3
    describe = summary("imdb_top_1000.csv")
    assert describe.loc["mean", "IMDB_Rating"] == 7.949299999999999
    assert describe.loc["max", "IMDB_Rating"] == 9.3


def test_Rating_graph():
    # df=read_file('imdb_top_1000.csv')
    # plt.hist(df['IMDB_Rating'])
    # plt.show()
    Rating_plot("imdb_top_1000.csv")


def test_MetaScore_graph():
    # df=read_file('imdb_top_1000.csv')
    # plt.hist(df['IMDB_Rating'])
    # plt.show()
    MetaScore_plot("imdb_top_1000.csv")
