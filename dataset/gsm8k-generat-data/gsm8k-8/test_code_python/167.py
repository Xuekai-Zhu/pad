def solution():
    # Calculate the length of Janet's previous movie in minutes
    prev_movie_length = 2 * 60

    # Calculate the length of Janet's newest movie in minutes
    newest_movie_length = prev_movie_length * 1.6

    # Calculate the cost per minute of filming Janet's previous movie
    prev_movie_cost_per_min = 50

    # Calculate the cost per minute of filming Janet's newest movie
    newest_movie_cost_per_min = 2 * prev_movie_cost_per_min

    # Calculate the total cost of filming Janet's previous movie
    prev_movie_cost = prev_movie_length * prev_movie_cost_per_min

    # Calculate the total cost of filming Janet's newest movie
    newest_movie_cost = newest_movie_length * newest_movie_cost_per_min

    # Calculate the total cost of filming Janet's entire newest film
    total_cost = prev_movie_cost + newest_movie_cost
    result = total_cost
    return result

print(solution())