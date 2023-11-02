def solution():
    # Convert 10 pounds to ounces
    ounces_needed = 10 * 16

    # Calculate the total number of cubes needed
    cubes_needed = ounces_needed / 2

    # Calculate the total number of hours needed to make all the cubes
    hours_needed = cubes_needed / 10

    # Calculate the total cost of running the ice maker
    total_cost = hours_needed * 1.5

    # Calculate the total cost of water
    water_cost = ounces_needed * 0.1

    # Calculate the total cost to make all the ice
    total_cost += water_cost
    result = total_cost
    return result

print(solution())