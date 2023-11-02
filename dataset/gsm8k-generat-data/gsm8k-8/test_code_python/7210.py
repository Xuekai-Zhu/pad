def solution():
    # Calculate the number of bags of chips needed
    chips_needed = 480 / 10 / 24
    # Round up to the nearest whole bag
    bags_needed = math.ceil(chips_needed)

    # Calculate the total cost of the bags
    total_cost = bags_needed * 2

    result = total_cost
    return result

print(solution())