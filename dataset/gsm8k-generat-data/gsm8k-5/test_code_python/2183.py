def solution():
    # Calculate the total number of planks Andrew needed without replacements
    total_planks = 8 + 20 + 11 + (8 - 2) + (2 * 4) + (2 * 4)

    # Calculate the number of planks Andrew had to replace
    replaced_planks = 2 * 3  # Both bedrooms had 3 planks each that needed to be replaced

    # Calculate the total number of planks Andrew used
    used_planks = total_planks + replaced_planks

    # Calculate the number of planks Andrew bought initially
    initial_planks = used_planks + 6  # Andrew had 6 planks left over

    result = initial_planks
    return result

print(solution())