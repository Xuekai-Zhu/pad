def solution():
    cable_cost = 15  # Jessica's basic cable service costs $15 per month
    movie_cost = 12  # The movie channels cost an additional $12 per month
    sports_cost = movie_cost - 3  # The sports channels cost $3 less per month than the movie channels

    # Calculate the total cost of adding both movie and sports channels
    total_cost = cable_cost + movie_cost + sports_cost

    result = total_cost
    return result

print(solution())