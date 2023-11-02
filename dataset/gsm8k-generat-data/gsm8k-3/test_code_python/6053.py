def solution():
    """Ron's baseball team scored 270 points in the year. There are 9 players on the team. If 5 of them averaged 50 points each, how many points did the remainder average?"""
    # Define the total number of players and points
    total_players = 9
    total_points = 270

    # Define the number of players and points accounted for
    accounted_players = 5
    accounted_points = accounted_players * 50

    # Calculate the number of remaining players and points
    remaining_players = total_players - accounted_players
    remaining_points = total_points - accounted_points

    # Calculate the average points for the remaining players
    average_points = remaining_points / remaining_players

    # Display the average points for the remaining players
    result = average_points
    return result

print(solution())