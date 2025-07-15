from functools import reduce

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
GENRES = [
    "action",
    "adventure",
    "animation",
    "biography",
    "comedy",
    "crime",
    "documentary",
    "drama",
    "family",
    "fantasy",
    "history",
    "horror",
    "music",
    "musical",
    "mystery",
    "romance",
    "sci-fi",
    "sport",
    "thriller",
    "war",
    "western"
]

def set_list_movies():
    movies_lst=[]
    while True:
        temp_movie=input("insert movie name: ")
        if temp_movie=="exit":
            break
        if temp_movie in movies_lst:
            print('movie already exists!')
            continue
        movies_lst.append(temp_movie)
    return movies_lst


def add_rating(movies_lst):
    movies_with_rating={}
    for m in movies_lst:
        while True:
            temp_rating = input("enter rating for the movie " + m + ": ")
            try:
                temp_rating=float(temp_rating)
                break
            except ValueError:
                print('rating must be an number!')

        movies_with_rating[m]=temp_rating
    return movies_with_rating


def get_basic_stats(movies_dict: dict):
    try:
        movies_dict=dict(sorted(movies_dict.items(), key=lambda x:x[1], reverse=True))
        rating_sum=0
        for rating in movies_dict.values():
            if isinstance(rating, list):
                rating_sum+=float(rating[0])
            else:
                rating_sum+=float(rating)

        avg = rating_sum / len(movies_dict)
        best_movie=list(movies_dict.keys())[0]
        worst_movie=list(movies_dict.keys())[-1]
        print(f"The best movie is: {GREEN}{best_movie}{RESET}")
        print(f"The worst movie is:{RED}{worst_movie}{RESET}")
        print(f"The average rating is:{YELLOW}{avg}{RESET}")
    except TypeError:
        print("not all ratings are numbers!")
    except AttributeError:
        print("your movie list is not a dict object!")


def add_genre(movies_dict:dict, movie_name:str):
    try:
        if movie_name in movies_dict.keys():
            genre=input(f'enter the genre of the movie {movie_name}: ')

            while genre.lower() not in GENRES:
                print("Your input is not a valid genre")
                genre = input(f'enter the genre of the movie {movie_name}: ')

            movies_dict[movie_name]=[movies_dict[movie_name], genre]
        else:
            print('the movie is not in your dict!')
        return movies_dict
    except AttributeError:
        print('your movies input is not in a dict format!')


def get_best_movie_by_genre(movies_dict:dict, genre:str):
    if genre.lower() not in GENRES:
        print("your input is not a known genre")
        return None
    if not isinstance(movies_dict, dict):
        print("your input is not a dict!")
        return  None
    try:
        best_rating=-1
        best_movie=""
        for movie in movies_dict:
            if not isinstance(movies_dict[movie], list):
                continue
            if movies_dict[movie][1]==genre:
                if float(movies_dict[movie][0])>best_rating:
                    best_rating=float(movies_dict[movie][0])
                    best_movie=movie
        return best_movie
    except ValueError:
        print('one of your movies rating is not numerical, '
              'please make sure each movie in your dict looks like: '
              '{<movie name>:[<rating>, <genre>]}')


def get_recommended_movies_by_genres(movies_dict:dict, fav_genres:list):
    movies_recommendations=[]
    for genre in fav_genres:
        if genre.lower() not in GENRES:
            print(f"The genre: {genre} is not a known genre!")
            continue
        best_movie=get_best_movie_by_genre(movies_dict, genre)
        if best_movie!="":
            movies_recommendations.append(f"the best {genre} movie is {best_movie}")
    return movies_recommendations


if __name__ == "__main__":
    movies = {
        "Gladiator": ["8.5", "action"],
        "Fight Club": ["8.8", "drama"],
        "Pulp Fiction": ["8.9", "crime"],
        "The Matrix": ["8.7", "sci-fi"],
        "The Prestige": ["8.5", "drama"],
        "Mad Max: Fury Road": ["8.1", "action"],
        "Joker": ["8.4", "crime"],
        "A Beautiful Mind": ["8.2", "biography"],
        "The Imitation Game": ["8.0", "biography"],
        "Blade Runner 2049": ["8.0", "sci-fi"]
    }

    get_basic_stats(movies)
    print("----------------------")
    for i in get_recommended_movies_by_genres(movies, ['crime', 'drama']):
        print(i)






