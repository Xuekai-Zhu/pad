def solution():
    
    # Define the number of movies watched on Saturday
    saturday_movies = 4

    # Calculate the number of movies watched on Sunday
    sunday_movies = saturday_movies / 2

    # Calculate the total number of movies watched in a week
    weekly_movies = saturday_movies + sunday_movies

    # Calculate the total number of movies watched in 4 weeks
    total_movies = weekly_movies * 4

    # return the result
    result = total_movies
    return result

print(solution())