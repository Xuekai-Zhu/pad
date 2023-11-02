def solution():
    # Calculate the length and cost of Janet's previous movie
    previous_movie_length = 120  # 2 hours long
    previous_movie_cost = previous_movie_length * 50  # $50 per minute

    # Calculate the length and cost of Janet's newest movie
    newest_movie_length = previous_movie_length + (0.6 * previous_movie_length)  # 60% longer than previous movie
    newest_movie_cost = newest_movie_length * 100  # twice as much per minute as previous movie

    # Calculate the total cost to film both movies
    total_cost = previous_movie_cost + newest_movie_cost
    result = total_cost
    return result

print(solution())