def solution():
    units_in_building = 100
    building_occupancy = 3/4
    units_occupied = units_in_building * building_occupancy
    rent_per_unit = 400
    total_rent = units_occupied * rent_per_unit
    return total_rent

print(solution())