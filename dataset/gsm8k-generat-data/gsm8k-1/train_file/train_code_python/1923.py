def solution():
    """Taro and Vlad play a video game competition together, earning 5 points for every win. After playing 30 rounds, Taro scored 4 points less than 3/5 of the total points scored. How many total points did Vlad score?"""
    rounds_played = 30
    points_per_win = 5
    total_points = rounds_played * 2 * points_per_win
    taro_points = (3/5) * total_points - 4
    vlad_points = total_points - taro_points
    result = vlad_points
    return result

print(solution())