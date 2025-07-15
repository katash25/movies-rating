from termcolor import colored
def set_list_movies():
    movies=[]
    while True:
        temp_movie=input("insert movie name: ")
        if temp_movie=="exit":
            break
        movies.append(temp_movie)
    return movies

def add_rating(movies):
    movies_with_rating={}
    for m in movies:
        temp_rating=input("enter rating for the movie "+m+": ")
        while type(temp_rating)!=int or type(temp_rating)!=float:
            print('rating must be an number!')
            temp_rating = input("enter rating for the movie: " + m)
        movies_with_rating[m]=temp_rating
    return sorted(movies_with_rating.items(), key=lambda x:x[1], reverse=True)

# def get_basic_stats(movies):



if __name__ == "__main__":
    movies=set_list_movies()
    movies=add_rating(movies)
    print(movies)



