def solution():
    regular_floors = 23 - 2  # Number of regular floors is total number of floors minus penthouse floors
    regular_units = regular_floors * 12  # Number of regular units is number of regular floors times 12 units per floor
    penthouse_units = 2 * 2  # Number of penthouse units is 2 floors times 2 units per floor
    total_units = regular_units + penthouse_units  # Total units is sum of regular units and penthouse units
    result = total_units
    return result

print(solution())