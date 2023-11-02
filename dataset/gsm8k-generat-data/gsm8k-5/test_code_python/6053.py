def solution():
    total_points = 270  # The team scored 270 points in the year
    num_players = 9  # There are 9 players on the team
    num_players_to_average = 5  # 5 players averaged 50 points each

    # Calculate the total points scored by the 5 players
    total_points_5 = num_players_to_average * 50

    # Calculate the total points scored by the remaining players
    total_points_remaining = total_points - total_points_5

    # Calculate the average points scored by the remaining players
    average_points_remaining = total_points_remaining / (num_players - num_players_to_average)

    result = average_points_remaining
    return result

print(solution())