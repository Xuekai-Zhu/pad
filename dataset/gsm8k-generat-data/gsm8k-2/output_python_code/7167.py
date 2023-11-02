def solution():
    """Wario is a field goal kicker on the high school football team. He attempts 60 field goals throughout the season. He misses 1/4 of the field goals. Of the field goals missed 20 percent were wide right. How many missed field goals went wide right?"""
    total_attempts = 60
    missed_percentage = 1/4
    missed_field_goals = total_attempts * missed_percentage
    wide_right_percentage = 0.2
    wide_right_misses = missed_field_goals * wide_right_percentage
    result = wide_right_misses
    return result

print(solution())