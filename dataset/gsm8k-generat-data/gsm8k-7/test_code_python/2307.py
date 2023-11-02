def solution():
    sandbox_length = 3
    sandbox_width = 3
    sand_area_per_bag = 3
    sand_cost_per_bag = 4.0

    # Calculate the total area of the sandbox
    sandbox_area = sandbox_length * sandbox_width

    # Calculate the number of bags of sand needed
    num_bags = sandbox_area / sand_area_per_bag

    # Calculate the total cost of sand
    total_cost = num_bags * sand_cost_per_bag
    result = total_cost
    return result

print(solution())