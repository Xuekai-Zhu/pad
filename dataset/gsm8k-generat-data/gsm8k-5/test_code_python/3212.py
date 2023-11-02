def solution():
    regular_floors = 23 - 2  # exclude top 2 penthouse floors
    regular_units = regular_floors * 12  # each regular floor has 12 units
    penthouse_units = 2 * 2  # top 2 floors have 2 penthouse units each

    # Calculate total number of units in the condo development
    total_units = regular_units + penthouse_units
    result = total_units
    return result

print(solution())