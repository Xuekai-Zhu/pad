def solution():
    # Calculate the total number of legs Borgnine has already seen
    legs_already_seen = 12 * 2 + 8 * 4 + 5 * 4  # number of legs for each animal

    # Calculate the number of tarantulas Borgnine needs to see
    tarantulas_needed = (1100 - legs_already_seen) / 8  # tarantulas have 8 legs
    result = tarantulas_needed
    return result

print(solution())