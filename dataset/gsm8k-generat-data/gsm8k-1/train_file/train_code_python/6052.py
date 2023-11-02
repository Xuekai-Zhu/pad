def solution():
    """Ron's baseball team scored 270 points in the year. There are 9 players on the team. If 5 of them averaged 50 points each, how many points did the remainder average?"""
    total_players = 9
    total_points = 270
    five_players_points = 5 * 50
    remainder_players = total_players - 5
    remainder_points = total_points - five_players_points
    remainder_average = remainder_points / remainder_players
    result = remainder_average
    return result

print(solution())