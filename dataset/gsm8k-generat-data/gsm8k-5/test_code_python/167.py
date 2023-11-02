def solution():
    previous_movie_length = 2  # Janet's previous movie was 2 hours long
    new_movie_length = previous_movie_length * 1.6  # Janet's new movie is 60% longer than the previous one

    # Calculate the cost to film the previous movie
    previous_movie_cost = 50 * 60 * previous_movie_length  # $50 per minute, 60 minutes per hour

    # Calculate the cost to film the new movie
    new_movie_cost = 2 * previous_movie_cost  # The new movie cost twice as much per minute to film as the previous one

    # Calculate the total amount of money required to film Janet's entire newest film
    total_cost = previous_movie_cost + new_movie_cost
    result = total_cost
    return result

print(solution())