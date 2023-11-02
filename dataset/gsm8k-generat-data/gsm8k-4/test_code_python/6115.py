def solution():
    """Pauly is making ice cubes. He needs 10 pounds of cubes. He knows that 2 ounces of water make 1 cube and each cube weighs 1/16th of a pound. It takes him 1 hour to make 10 cubes. Every hour his ice maker run costs $1.50. Every ounce of water costs $0.10. How much will it cost to make all the ice?"""
    # Define the total amount of water required to make 10 pounds of ice cubes
    total_water = 10 * 16 * 2

    # Calculate the cost of the water
    water_cost = total_water * 0.10

    # Calculate the cost of running the ice maker for 1 hour
    hourly_cost = 1.50

    # Calculate the total time required to make all the ice cubes
    total_time = (10 / 10) * 1

    # Calculate the total cost
    total_cost = water_cost + (hourly_cost * total_time)

    result = total_cost
    return result

print(solution())