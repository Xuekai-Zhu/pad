def solution():
    """Josh wants to build a square sandbox that is 3 ft long, 3 ft wide for his son. He can buy sand in 3 sq ft bags for $4.00 a bag. How much will it cost him to fill up the sandbox?"""
    # Calculate the area of the sandbox
    sandbox_area = 3 * 3

    # Calculate the number of bags needed to fill the sandbox
    bags_needed = sandbox_area / 3

    # Calculate the total cost of the sand
    sand_cost = bags_needed * 4.00

    result = sand_cost
    return result

print(solution())