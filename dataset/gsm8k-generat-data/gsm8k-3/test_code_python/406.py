def solution():
    """Joseph and his friends watched two movies in his house. The first movie is 1 hour and 30 minutes long while the second movie is 30 minutes longer than the first. Before the movies, they spent 10 minutes making popcorn and twice as long making fries. How long, in hours, did it take Joseph and his friends to cook and watch the movies?"""
    # Define the length of the first movie and calculate the length of the second movie
    movie1_length = 1.5 # hours
    movie2_length = movie1_length + 0.5 # 30 minutes longer

    # Calculate the total watching time
    total_watching_time = movie1_length + movie2_length

    # Calculate the cooking time
    popcorn_time = 10 / 60 # convert 10 minutes to hours
    fries_time = 2 * popcorn_time
    cooking_time = popcorn_time + fries_time

    # Calculate the total time
    total_time = total_watching_time + cooking_time

    # Display the total time
    result = total_time
    return result

print(solution())