def solution():
    
    num_screens = 6
    theater_hours = 8
    movie_duration = 2
    movies_per_screen = theater_hours // movie_duration
    total_movies = movies_per_screen * num_screens
    result = total_movies
    return result

print(solution())