def solution():
    """Wario attempts 60 field goals throughout the season. He misses 1/4 of the field goals. Of the field goals missed 20 percent were wide right. How many missed field goals went wide right?"""
    # Define the number of field goals attempted
    total_attempts = 60

    # Calculate the number of field goals missed
    missed_goals = total_attempts * 0.25

    # Calculate the number of missed field goals that went wide right
    wide_right_goals = missed_goals * 0.2

    # Display the number of missed field goals that went wide right
    result = wide_right_goals
    return result

print(solution())