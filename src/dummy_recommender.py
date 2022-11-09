"""
random selector
"""

import random

def random_choice(df_movies, number=10):
    """
    doing random selection from dataframe
    """
    all_movies=list(df_movies["title"].unique())
    return random.choices(all_movies, k=number)



if __name__ == "__main__":
    import pandas as pd

    DATAPATH="../data/"


    DF_MOVIES=pd.read_csv(DATAPATH+"movies.csv")

    selection=random_choice(DF_MOVIES)

    print("the following movies have been selected for you:")
    for movie in selection:
        print(movie)
