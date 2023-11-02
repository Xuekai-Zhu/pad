def solution():
    """Joseph and his friends watched two movies in his house. The first movie is 1 hour and 30 minutes long while the second movie is 30 minutes longer than the first. Before the movies, they spent 10 minutes making popcorn and twice as long making fries. How long, in hours, did it take Joseph and his friends to cook and watch the movies?"""
    # Define the length of the first movie
    first_movie_length = 90 # minutes

    # Calculate the length of the second movie
    second_movie_length = first_movie_length + 30 # minutes

    # Calculate the total length of the movies
    total_movie_length = first_movie_length + second_movie_length # minutes

    # Define the time spent making popcorn and fries
    popcorn_time = 10 # minutes
    fries_time = 2 * popcorn_time # minutes

    # Calculate the total time spent cooking and watching movies
    total_time = total_movie_length + popcorn_time + fries_time # minutes

    # Convert the time to hours
    total_time_hours = total_time / 60 # hours

    # return the result
    result = total_time_hours
    return result

print(solution())