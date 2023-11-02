def solution():
    """Wario is a field goal kicker on the high school football team. He attempts 60 field goals throughout the season. He misses 1/4 of the field goals. Of the field goals missed 20 percent were wide right. How many missed field goals went wide right?"""
    # Define the total number of field goal attempts
    total_attempts = 60

    # Calculate the number of field goals missed
    missed_goals = total_attempts * (1/4)

    # Calculate the number of missed goals that went wide right
    wide_right = missed_goals * 0.2

    result = wide_right
    return result

print(solution())