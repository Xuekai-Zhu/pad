def solution():
    layla_goals = 104  # Layla scored 104 goals in four games
    kristin_goals = layla_goals - 24  # Kristin scored 24 fewer goals than Layla

    # Calculate the total number of goals scored by both players
    total_goals = layla_goals + kristin_goals

    # Calculate the average number of goals they scored
    average_goals = total_goals / 2
    result = average_goals
    return result

print(solution())