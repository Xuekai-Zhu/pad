def solution():
    goal = 30
    monday_situps = 12
    tuesday_situps = 19

    # Calculate the total situps done so far
    total_situps = monday_situps + tuesday_situps

    # Calculate how many situps Shawna needs to do on Wednesday
    remaining_situps = goal - total_situps

    result = remaining_situps
    return result

print(solution())