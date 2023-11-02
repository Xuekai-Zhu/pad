def solution():
    # Find the points scored at the first away game
    points_first_away = 62 / 2

    # Find the points scored at the second away game
    points_second_away = points_first_away + 18

    # Find the points scored at the third away game
    points_third_away = points_second_away + 2

    # Find the cumulative points after the last home game
    cumulative_points = 62 + points_first_away + points_second_away + points_third_away

    # Find the score needed to bring cumulative points up to four times the last home game's score
    score_needed = 4 * 62 - cumulative_points

    result = score_needed
    return result

print(solution())