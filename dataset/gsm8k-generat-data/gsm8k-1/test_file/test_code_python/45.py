def solution():
    """Richard lives in an apartment building with 15 floors. Each floor contains 8 units, and 3/4 of the building is occupied. What's the total number of unoccupied units In the building?"""
    num_floors = 15
    units_per_floor = 8
    total_units = num_floors * units_per_floor
    occupied_percent = 3/4
    occupied_units = total_units * occupied_percent
    unoccupied_units = total_units - occupied_units
    result = unoccupied_units
    return result

print(solution())