def solution():
    # Calculate the number of sit-ups Barney can do in one minute
    barney_situps = 45

    # Calculate the number of sit-ups Carrie can do in one minute
    carrie_situps = 2 * barney_situps

    # Calculate the number of sit-ups Jerrie can do in one minute
    jerrie_situps = carrie_situps + 5

    # Calculate the total number of sit-ups performed
    total_situps = (barney_situps * 1) + (carrie_situps * 2) + (jerrie_situps * 3)
    result = total_situps
    return result

print(solution())