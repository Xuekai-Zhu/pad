def solution():
    # Define the cost of a pack of pretzels and the percentage increase for chips
    pretzel_cost = 4
    chip_increase = 0.75

    # Calculate the cost of a pack of chips and the total cost for Maciek's purchases
    chip_cost = pretzel_cost * (1 + chip_increase)
    total_cost = 2 * chip_cost + 2 * pretzel_cost

    result = total_cost
    return result

print(solution())