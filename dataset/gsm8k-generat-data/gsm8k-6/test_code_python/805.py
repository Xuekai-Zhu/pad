def solution():
    # Calculate the total number of movies shown in the theater in one day
    movies_per_screen = 8 // 2  # each screen shows movies for 8 hours and each movie lasts 2 hours
    total_movies = movies_per_screen * 6  # there are 6 screens in total
    result = total_movies
    return result

print(solution())