import movies

USERS={}


class User:
    MOVIE_GALLERY = movies.gallery
    def __init__(self, user_name):
        self.user_name=user_name
        self.movies_dict=self.build_user_ratings()

    @staticmethod
    def build_user_ratings():
        movies_dict={}
        for movie in User.MOVIE_GALLERY.movie_dict.values():
            while True:
                rating = input(f"enter your rating to the movie {movie.movie_name}, or press enter to continue: ")
                if rating == "":
                    break
                try:
                    rating=float(rating)
                    if rating < 0 or rating > 10:
                        print("rating must be between 0 and 10")
                        continue
                    movies_dict[movie] = rating
                    break
                except ValueError:
                    print(f"invalid rating {rating}, please enter a number")

        return movies_dict

    def __str__(self):
        user_str=""
        for movie in list(self.movies_dict.items()):
            user_str+=f"{movie[0].movie_name} --> {movie[1]}\n"
        return user_str

if __name__=="__main__":
    yair= User('yair')
    print(yair)










