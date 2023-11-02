def solution():
    
    screens = 6
    hours_open = 8
    movie_length = 2
    movies_per_screen = hours_open // movie_length
    total_movies = movies_per_screen * screens
    result = total_movies
    return result

print(solution())