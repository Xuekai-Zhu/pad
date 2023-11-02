def solution():
    """If Layla scored 104 goals in four hockey games and Kristin scored 24 fewer goals in the same four games, calculate the average number of goals the two scored."""
    layla_goals = 104
    kristin_goals = layla_goals - 24
    total_goals = layla_goals + kristin_goals
    games_played = 4
    avg_goals = total_goals / (games_played * 2)
    result = avg_goals
    return result

print(solution())