def solution():
    # Calculate the total points scored by the 5 players
    points_by_5 = 5 * 50  

    # Calculate the points scored by the remaining players
    points_by_remainder = 270 - points_by_5  

    # Calculate the average points scored by the remaining players
    average_by_remainder = points_by_remainder / 4  # 4 players remain after the 5 players who scored 50 points each
    result = average_by_remainder
    return result

print(solution())