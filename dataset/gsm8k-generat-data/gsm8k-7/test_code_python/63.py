def solution():
    workout_goal = 30
    situps_monday = 12
    situps_tuesday = 19

    # Calculate the total number of situps Shawna has done so far
    total_situps = situps_monday + situps_tuesday

    # Calculate the remaining number of situps for Shawna to meet her goal
    remaining_situps = workout_goal - total_situps

    result = remaining_situps
    return result

print(solution())