def solution():
    # Calculate the total time of all players' video
    total_time = 130 + 145 + 85 + 60 + 180  # in seconds

    # Calculate the average time for each player
    average_time = total_time / 5  # there are 5 players
    average_time_in_minutes = average_time / 60  # convert seconds to minutes
    result = average_time_in_minutes
    return result

print(solution())