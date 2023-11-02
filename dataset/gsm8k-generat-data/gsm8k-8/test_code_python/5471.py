def solution():
    # Calculate the number of minutes Diana did situps for
    diana_minutes = 40 / 4

    # Calculate Hani's situp rate
    hani_rate = 4 + 3

    # Calculate the total number of situps Hani did
    hani_situps = hani_rate * diana_minutes

    # Calculate the total number of situps they did together
    total_situps = hani_situps + 40
    result = total_situps
    return result

print(solution())