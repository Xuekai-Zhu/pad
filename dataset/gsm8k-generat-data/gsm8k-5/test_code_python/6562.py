def solution():
    pretzel_cost = 4  # Pack of pretzels costs $4
    chip_cost = 1.75 * pretzel_cost  # Pack of chips is 75% more expensive than pack of pretzels

    # Calculate the total cost of Maciek's purchases
    total_cost = (2 * pretzel_cost) + (2 * chip_cost)

    result = total_cost
    return result

print(solution())