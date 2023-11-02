def solution():
    # Calculate the total points scored by the 5 players who averaged 50 points each
    total_points_by_5_players = 5 * 50

    # Calculate the total points scored by the remaining 4 players
    total_points_by_remaining_players = 270 - total_points_by_5_players

    # Calculate the average points scored by the remaining players
    remaining_players_average = total_points_by_remaining_players / 4
    result = remaining_players_average
    return result

print(solution())