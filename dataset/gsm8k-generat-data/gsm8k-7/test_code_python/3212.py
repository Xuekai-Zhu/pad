def solution():
    num_regular_floors = 21  # 23 floors - 2 penthouse floors
    num_penthouse_floors = 2
    num_regular_units_per_floor = 12
    num_penthouse_units_per_floor = 2

    # Calculate the total number of regular units in the condo
    total_regular_units = num_regular_floors * num_regular_units_per_floor

    # Calculate the total number of penthouse units in the condo
    total_penthouse_units = num_penthouse_floors * num_penthouse_units_per_floor

    # Calculate the total number of units in the condo
    total_units = total_regular_units + total_penthouse_units
    result = total_units
    return result

print(solution())