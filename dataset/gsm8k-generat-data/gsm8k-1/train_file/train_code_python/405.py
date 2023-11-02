def solution():
    """Joseph and his friends watched two movies in his house. The first movie is 1 hour and 30 minutes long while the second movie is 30 minutes longer than the first. Before the movies, they spent 10 minutes making popcorn and twice as long making fries. How long, in hours, did it take Joseph and his friends to cook and watch the movies?"""
    movie_1_length = 90 # minutes
    movie_2_length = movie_1_length + 30 # minutes
    cooking_time = (10 + 2*10) # minutes
    total_time = (movie_1_length + movie_2_length + cooking_time) / 60 # hours
    result = total_time
    return result

print(solution())