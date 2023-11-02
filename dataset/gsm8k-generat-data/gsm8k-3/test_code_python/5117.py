def solution():
    """Mr. Resty has two identical 4-story buildings. The first floor has 2 apartment units while the rest of the floors have 5 apartment units on each floor. How many apartment units does Mr. Resty have in all?"""
    # Find the number of apartment units on each of the 3 upper floors
    apartment_units_per_floor = 5

    # Calculate the number of apartment units on the first floor
    first_floor_apartment_units = 2

    # Calculate the total number of apartment units on each building
    total_apartment_units_per_building = (apartment_units_per_floor * 3) + first_floor_apartment_units

    # Calculate the total number of apartment units for both buildings
    total_apartment_units = total_apartment_units_per_building * 2

    # Display the total number of apartment units
    result = total_apartment_units
    return result

print(solution())