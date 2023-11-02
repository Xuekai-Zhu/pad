def solution():
    # Calculate the total time for all players
    total_time = 130 + 145 + 85 + 60 + 180  # Total time in seconds

    # Convert the total time to minutes
    total_time = total_time / 60

    # Calculate the average time for each player
    average_time = total_time / 5

    result = average_time
    return result

print(solution())