def solution():
    
    # Define the initial amount of water in the pool
    initial_water = 10000

    # Calculate the amount of water in the tank after the water pump and Anthony and his father fill them
    water_after_pump = initial_water / 2
    water_after_anthony = water_after_pump / 2
    water_after_father = water_after_pump / 2

    # Calculate the total amount of water remaining in the tank after 6 days
    remaining_water = water_after_anthony + water_after_father

    # Display the total amount of water remaining in the tank
    result = remaining_water
    return result

print(solution())