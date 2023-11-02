def solution():
    total_attempts = 60  # Wario attempts 60 field goals throughout the season
    field_goals_missed = total_attempts * (1/4)  # Wario misses 1/4 of the field goals
    wide_right_misses = field_goals_missed * 0.2  # 20% of missed field goals were wide right
    result = wide_right_misses
    return result

print(solution())