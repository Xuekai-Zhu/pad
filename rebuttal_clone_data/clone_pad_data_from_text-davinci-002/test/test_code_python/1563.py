def solution():
    hours_played = 2
    minutes_per_point = 5
    points_needed = 8
    total_points = hours_played * 60 / minutes_per_point
    games_won = total_points / points_needed
    result = games_won
    return result

print(solution())