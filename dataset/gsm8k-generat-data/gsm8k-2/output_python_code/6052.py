def solution():
    """Ron's baseball team scored 270 points in the year. There are 9 players on the team. If 5 of them averaged 50 points each, how many points did the remainder average?"""
    total_points = 270
    total_players = 9
    avg_points_5 = 50
    total_points_5 = avg_points_5 * 5
    total_points_remainder = total_points - total_points_5
    total_players_remainder = total_players - 5
    avg_points_remainder = total_points_remainder / total_players_remainder
    result = avg_points_remainder
    return result

print(solution())