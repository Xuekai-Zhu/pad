def solution():
    """If Layla scored 104 goals in four hockey games and Kristin scored 24 fewer goals in the same four games, calculate the average number of goals the two scored."""
    # Calculate Kristin's total number of goals
    kristin_goals = 104 - 24

    # Calculate the total number of goals scored by both Layla and Kristin
    total_goals = 104 + kristin_goals

    # Calculate the average number of goals scored by both Layla and Kristin
    average_goals = total_goals / 2

    # return the result
    result = average_goals
    return result

print(solution())