def solution():
    """Wario is a field goal kicker on the high school football team. He attempts 60 field goals throughout the season. He misses 1/4 of the field goals. Of the field goals missed 20 percent were wide right. How many missed field goals went wide right?"""
    total_field_goals = 60
    missed_field_goals = total_field_goals / 4
    wide_right_misses = missed_field_goals * 0.2
    result = wide_right_misses
    return result

print(solution())