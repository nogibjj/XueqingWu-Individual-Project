from mylib.lib import read_file, Rating_plot, MetaScore_plot

def test_read_file():
    df=read_file('imdb_top_1000.csv')
    # assert not df.empty()
    assert len(df)==1000

def test_Rating_graph():
    # df=read_file('imdb_top_1000.csv')
    # plt.hist(df['IMDB_Rating'])
    # plt.show()
    Rating_plot('imdb_top_1000.csv')

def test_MetaScore_graph():
    # df=read_file('imdb_top_1000.csv')
    # plt.hist(df['IMDB_Rating'])
    # plt.show()
    MetaScore_plot('imdb_top_1000.csv')

