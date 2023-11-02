def solution():
    """Joseph and his friends watched two movies in his house. The first movie is 1 hour and 30 minutes long while the second movie is 30 minutes longer than the first. Before the movies, they spent 10 minutes making popcorn and twice as long making fries. How long, in hours, did it take Joseph and his friends to cook and watch the movies?"""
    movie1_length = 90 / 60      # in hours
    movie2_length = (90 + 30) / 60      # in hours
    total_movie_length = movie1_length + movie2_length
    popcorn_time = 10 / 60      # in hours
    fries_time = 2 * popcorn_time
    total_cook_time = popcorn_time + fries_time
    total_time = total_cook_time + total_movie_length
    result = total_time
    return result

print(solution())