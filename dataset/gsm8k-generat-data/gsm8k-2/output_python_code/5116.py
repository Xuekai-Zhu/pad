def solution():
    """Mr. Resty has two identical 4-story buildings. The first floor has 2 apartment units while the rest of the floors have 5 apartment units on each floor. How many apartment units does Mr. Resty have in all?"""
    first_floor_units = 2
    upper_floor_units = 5 * 3
    total_units_per_building = first_floor_units + upper_floor_units
    total_units = 2 * total_units_per_building
    result = total_units
    return result

print(solution())