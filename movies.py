MOVIES = [
    "Inception",
    "The Matrix",
    "Forrest Gump",
    "Gladiator",
    "The Godfather"
]
"""class that saves name and genre of a movie"""
class Movie:
    def __init__(self, movie_name:str, movie_genre:str=""):
        self.movie_name = movie_name
        self.movie_genre = movie_genre

    def __str__(self):
        return f"{self.movie_name} ({self.movie_genre})"

"""class that stores dict of movies in the form {<movie name> : <Movie object>}"""
class MovieGallery:
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
    def __init__(self, movie_dict:dict[str, Movie]=None):
        self.movie_dict = movie_dict
        self.movie_genres = MovieGallery.GENRES

    """function that add movie to a movie gallery"""
    def add_movie(self, movie:Movie):
        if not isinstance(movie, Movie):
            print(f"Invalid type: {type(movie)}")
            return False
        if movie.movie_name not in self.movie_dict:
            self.movie_dict[movie.movie_name] = movie
            return True
        print(f"{movie.movie_name} already exists")
        return False

    """function that allow user to change genre of movie in his gallery"""
    def update_genre(self, movie:Movie, new_genre:str):
        if not isinstance(movie, Movie):
            print(f"Invalid type: {type(movie)}")
            return False
        if movie.movie_name not in self.movie_dict.keys():
            self.movie_dict[movie.movie_name] = Movie(movie.movie_name, new_genre)
            return True
        print(f"{movie.movie_name} not exists in gallery")
        return False

    def __str__(self):
        return "The movies in this gallery:\n"+"\n".join(str(movie) for movie in self.movie_dict.values())


"""add to a list all the movies input from user, stops when user input 'exit' """
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

"""function that init the basic movie gallery, gets list of movies, return an MovieGallery object"""
def init_gallery(movie_lst:list):
    try:
        movie_dict = {}
        for movie in movie_lst:
            genre = input(f"insert genre for '{movie}': ")
            while genre not in MovieGallery.GENRES:
                print(f"Invalid genre: {genre}")
                genre = input(f"insert genre for '{movie}': ")
            new_movie = Movie(movie, movie_genre=genre)
            movie_dict[new_movie.movie_name] = new_movie
        return MovieGallery(movie_dict)

    except ValueError as ve:
        print(f"Invalid input: {ve}")

    except TypeError as te:
        print(f"Type error: {te}")

    except EOFError:
        print("Input cancelled (EOF).")

    except KeyboardInterrupt:
        print("\nInput interrupted by user.")

gallery=init_gallery(MOVIES)







