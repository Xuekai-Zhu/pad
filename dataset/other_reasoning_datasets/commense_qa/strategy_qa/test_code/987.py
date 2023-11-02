def solution():
    years_since_discovery = 2021 - 2010 # assuming the current year is 2021
    rotation_duration = 6
    rotations_completed = years_since_discovery / rotation_duration
    if rotations_completed < 2:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())