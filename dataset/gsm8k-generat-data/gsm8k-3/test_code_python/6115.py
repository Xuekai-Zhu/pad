def solution():
    """Pauly is making ice cubes. He needs 10 pounds of cubes. He knows that 2 ounces of water make 1 cube and each cube weighs 1/16th of a pound. It takes him 1 hour to make 10 cubes. Every hour his ice maker run costs $1.50. Every ounce of water costs $0.10. How much will it cost to make all the ice?"""
    # Define the number of cubes needed and the amount of water per cube
    cubes_needed = 10
    water_per_cube = 2  # 2 ounces per cube

    # Calculate the total water needed in ounces
    water_needed = cubes_needed * water_per_cube

    # Calculate the cost of the water
    water_cost = water_needed * 0.1  # $0.10 per ounce

    # Calculate the cost of running the ice maker
    ice_maker_cost = 1.5  # $1.50 per hour

    # Calculate the time needed to make all the cubes
    time_needed = cubes_needed / 10  # 10 cubes per hour

    # Calculate the cost of running the ice maker for the necessary amount of time
    total_ice_maker_cost = time_needed * ice_maker_cost

    # Calculate the total cost of making all the ice cubes
    total_cost = water_cost + total_ice_maker_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())