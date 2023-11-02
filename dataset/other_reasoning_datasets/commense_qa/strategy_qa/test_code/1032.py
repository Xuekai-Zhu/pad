def solution():
    clark_gable_movies = [] # list of movies Clark Gable appeared in
    john_williams_movies = [] # list of movies scored by John Williams
    # check if there are any common movies in both lists
    common_movies = set(clark_gable_movies) & set(john_williams_movies)
    if common_movies:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())