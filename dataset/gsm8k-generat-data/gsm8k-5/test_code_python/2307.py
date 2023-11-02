def solution():
    # Calculate the area of the sandbox
    sandbox_area = 3 * 3  # A square sandbox with 3ft length and width has an area of 9 sq ft

    # Calculate the number of bags of sand Josh needs to buy
    bags_of_sand = sandbox_area / 3  # Each bag contains 3 sq ft of sand

    # Calculate the total cost of the sand
    sand_cost = bags_of_sand * 4  # Each bag costs $4.00

    result = sand_cost
    return result

print(solution())