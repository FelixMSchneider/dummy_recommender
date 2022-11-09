def random_choice(df_movies, number=10):
    import random
    all_movies=list(df_movies["title"].unique())
    return random.choices(all_movies, k=number)



if __name__ == "__main__":
    import pandas as pd

    datapath="../data/"


    df_movies=pd.read_csv(datapath+"movies.csv")

    selection=random_choice(df_movies)

    print("the following movies have been selected for you:")
    for movie in selection:
        print(movie)

    
