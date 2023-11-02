def solution():
    """Jill and her friends watch 4 movies every Saturday and half the number of movies on Sunday than on Saturday. If they watch movies every weekend,how many movies can they watch in 4 weeks?"""
    saturday_movies = 4
    sunday_movies = saturday_movies / 2
    weekend_movies = saturday_movies + sunday_movies
    weeks = 4
    total_movies = weekend_movies * 2 * weeks
    result = total_movies
    return result

print(solution())