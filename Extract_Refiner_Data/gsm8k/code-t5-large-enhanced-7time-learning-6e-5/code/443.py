def solution():
    
    # Define the initial points for Joey and Marcy
    joey_points = 214
    marcy_points = 225

    # Calculate the points scored by Joey and Marcy
    joey_score = 26
    marcy_score = 10

    # Calculate the total points scored by Joey and Marcy
    total_score = joey_score + marcy_score

    # Calculate the points Joey is currently winning
    winning_points = joey_points - total_score

    # return the result
    result = winning_points
    return result

print(solution())