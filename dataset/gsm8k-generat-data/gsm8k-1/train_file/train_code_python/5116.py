def solution():
    """Mr. Resty has two identical 4-story buildings. The first floor has 2 apartment units while the rest of the floors have 5 apartment units on each floor. How many apartment units does Mr. Resty have in all?"""
    floors_per_building = 4
    units_on_first_floor = 2
    units_per_floor = 5
    total_units_per_building = (floors_per_building - 1) * units_per_floor + units_on_first_floor
    total_units = total_units_per_building * 2
    result = total_units
    return result

print(solution())