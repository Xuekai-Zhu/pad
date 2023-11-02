def solution():
    """Ron's baseball team scored 270 points in the year. There are 9 players on the team. If 5 of them averaged 50 points each, how many points did the remainder average?"""
    # Define the total number of points and players on the team
    total_points = 270
    total_players = 9

    # Define the number of players who averaged 50 points each
    num_players_50 = 5

    # Calculate the total number of points scored by the 5 players
    total_points_50 = num_players_50 * 50

    # Calculate the total number of points scored by the remaining players
    remaining_points = total_points - total_points_50

    # Calculate the number of remaining players
    num_remaining_players = total_players - num_players_50

    # Calculate the average points scored by the remaining players
    remaining_average = remaining_points / num_remaining_players

    # return the result
    result = remaining_average
    return result

print(solution())