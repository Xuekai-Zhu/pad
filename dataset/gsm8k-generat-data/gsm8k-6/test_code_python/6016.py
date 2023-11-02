def solution():
    # Calculate the total distance covered by Madison and Gigi in 6 laps each
    total_distance = 2 * 6 * 150  # 2 because there are 2 people running

    # Calculate the remaining distance
    remaining_distance = 2400 - total_distance

    # Calculate the number of laps required to cover the remaining distance
    remaining_laps = remaining_distance / 150

    result = remaining_laps
    return result

print(solution())