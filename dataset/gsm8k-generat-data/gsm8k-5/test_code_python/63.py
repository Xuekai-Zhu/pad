def solution():
    goal = 30  # Shawna's workout goal is 30 situps
    monday_situps = 12  # Shawna did 12 situps on Monday
    tuesday_situps = 19  # Shawna did 19 situps on Tuesday
    situps_remaining = goal - monday_situps - tuesday_situps  # Situps still needed to meet the goal

    # Shawna needs to do this many situps on Wednesday to meet her goal
    wednesday_situps = situps_remaining + goal

    result = wednesday_situps
    return result

print(solution())