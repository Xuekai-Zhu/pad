def solution():
    """Mr. Resty has two identical 4-story buildings. The first floor has 2 apartment units while the rest of the floors have 5 apartment units on each floor. How many apartment units does Mr. Resty have in all?"""
    # Define the number of floors and apartment units per floor
    floors = 4
    units_first_floor = 2
    units_per_floor = 5

    # Calculate the total number of apartment units per building
    total_units_per_building = (floors - 1) * units_per_floor + units_first_floor

    # Calculate the total number of apartment units for both buildings
    total_units = total_units_per_building * 2

    # Return the result
    result = total_units
    return result

print(solution())