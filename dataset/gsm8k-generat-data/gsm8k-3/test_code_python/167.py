def solution():
    """Janet filmed a new movie that is 60% longer than her previous 2-hour long movie. Her previous movie cost $50 per minute to film, and the newest movie cost twice as much per minute to film as the previous movie. What was the total amount of money required to film Janet's entire newest film?"""
    # Define the length of the previous movie and the percentage increase of the new movie
    previous_movie_length = 120  # minutes
    percentage_increase = 60  # %

    # Calculate the length of the new movie and the increase
    new_movie_length = previous_movie_length * (1 + (percentage_increase / 100))
    increase = new_movie_length - previous_movie_length

    # Calculate the cost per minute of the previous movie and the new movie
    previous_cost_per_minute = 50  # dollars
    new_cost_per_minute = previous_cost_per_minute * 2

    # Calculate the total cost of filming the previous movie and the new movie
    previous_movie_cost = previous_movie_length * previous_cost_per_minute
    new_movie_cost = new_movie_length * new_cost_per_minute

    # Calculate the total cost of filming Janet's entire newest movie
    total_cost = previous_movie_cost + new_movie_cost

    # Return the result
    result = total_cost
    return result

print(solution())