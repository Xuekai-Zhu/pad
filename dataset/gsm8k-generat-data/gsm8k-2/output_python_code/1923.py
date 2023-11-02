def solution():
    """Taro and Vlad play a video game competition together, earning 5 points for every win. After playing 30 rounds, Taro scored 4 points less than 3/5 of the total points scored. How many total points did Vlad score?"""
    rounds = 30
    taro_points = (3/5) * (rounds * 5) - 4
    total_points = rounds * 5 * 2
    vlad_points = total_points - taro_points
    result = vlad_points
    return result

print(solution())