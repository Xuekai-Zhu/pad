def solution():
    # Calculate the total number of units in the condo
    regular_floors = 23 - 2  # exclude the top 2 floors for penthouse units
    regular_units = regular_floors * 12  # regular floors have 12 units each
    penthouse_units = 2 * 2  # top 2 floors have 2 penthouse units each
    total_units = regular_units + penthouse_units
    result = total_units
    return result

print(solution())