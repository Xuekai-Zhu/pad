def solution():
    previous_movie_length = 120  # in minutes
    new_movie_length = previous_movie_length * 1.6  # 60% longer
    previous_movie_cost_per_minute = 50
    new_movie_cost_per_minute = previous_movie_cost_per_minute * 2  # double the cost

    # Calculate the cost of filming the previous movie
    previous_movie_cost = previous_movie_length * previous_movie_cost_per_minute

    # Calculate the cost of filming the new movie
    new_movie_cost = new_movie_length * new_movie_cost_per_minute

    # Calculate the total amount of money required to film Janet's entire newest film
    total_cost = previous_movie_cost + new_movie_cost
    result = total_cost
    return result

print(solution())