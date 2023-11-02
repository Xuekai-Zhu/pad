def solution():
    total_pounds = 10
    total_cubes = total_pounds * 16  # There are 16 cubes per pound
    water_per_cube = 2 / 16  # 2 ounces of water make 1 cube, and 1 cube weighs 1/16th of a pound
    water_needed = total_cubes * water_per_cube

    hourly_cost = 1.50  # The cost to run the ice maker for 1 hour
    water_cost_per_ounce = 0.10  # The cost of 1 ounce of water

    # Calculate the total cost of making the ice
    total_cost = (hourly_cost * (total_pounds / 10)) + (water_cost_per_ounce * water_needed)
    result = total_cost
    return result

print(solution())