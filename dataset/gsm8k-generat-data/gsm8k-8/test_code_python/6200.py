def solution():
    # Calculate the number of units built in the first half of the year
    first_half_units = 2000 * 3/5

    # Calculate the total units built by October
    total_units_built = first_half_units + 300

    # Calculate the remaining units to be built
    remaining_units = 2000 - total_units_built
    result = remaining_units
    return result

print(solution())