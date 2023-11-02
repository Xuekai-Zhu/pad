def solution():
    # Calculate the number of ounces of water needed to make 10 pounds of ice
    water_needed = 10 * 16 * 2  # 2 ounces of water make 1 cube and 1 cube weighs 1/16th of a pound

    # Calculate the cost of water
    water_cost = water_needed * 0.10

    # Calculate the cost of running the ice maker for 1 hour
    running_cost = 1.50

    # Calculate the total cost of making 10 pounds of ice
    total_cost = water_cost + running_cost

    result = total_cost
    return result

print(solution())