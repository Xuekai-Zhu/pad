def solution():
    num_floors = 4
    units_per_floor = 5
    units_on_first_floor = 2
    total_units_per_building = (num_floors - 1) * units_per_floor + units_on_first_floor
    total_units = total_units_per_building * 2
    return total_units

print(solution())