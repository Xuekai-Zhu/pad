def solution():
    
    # Define the number of floors and units per floor
    floors = 15
    units_per_floor = 8

    # Calculate the total number of units in the building
    total_units = floors * units_per_floor

    # Calculate the number of occupied units
    occupied_units = total_units * 0.75

    # Calculate the number of unoccupied units
    unoccupied_units = total_units - occupied_units

    # Display the total number of unoccupied units
    result = unoccupied_units
    return result

print(solution())