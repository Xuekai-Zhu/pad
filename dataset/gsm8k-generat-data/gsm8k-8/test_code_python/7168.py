def solution():
    # Calculate the number of field goals missed
    missed_goals = 60 * (1/4)

    # Calculate the number of missed field goals that went wide right
    wide_right_goals = missed_goals * 0.2

    result = wide_right_goals
    return result

print(solution())