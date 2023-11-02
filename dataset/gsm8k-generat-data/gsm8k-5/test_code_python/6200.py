def solution():
    total_units = 2000  # The contracted number of houses to be built is 2000
    first_half_units = 3/5 * total_units  # The first half of the year, the company built 3/5 of the total units
    units_built_by_oct = 300  # By October, the company built an additional 300 units

    # Calculate the total units built by the company
    total_built_units = first_half_units + units_built_by_oct

    # Calculate the units remaining from the contracted number
    remaining_units = total_units - total_built_units
    result = remaining_units
    return result

print(solution())