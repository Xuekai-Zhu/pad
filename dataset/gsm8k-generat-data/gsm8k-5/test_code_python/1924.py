def solution():
    rounds_played = 30  # Taro and Vlad played 30 rounds
    points_per_win = 5  # They earned 5 points for every win
    total_points = rounds_played * points_per_win  # Calculate the total points scored

    # Calculate Taro's score
    taro_score = (3/5) * total_points - 4

    # Calculate Vlad's score
    vlad_score = total_points - taro_score
    result = vlad_score
    return result

print(solution())