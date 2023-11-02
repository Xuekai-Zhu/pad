def solution():
    # Calculate the cost of two packets of pretzels
    pretzel_cost = 4 * 2  # two packs of pretzels at $4 per pack

    # Calculate the cost of two packets of chips
    chip_cost = (4 * 1.75) * 2  # two packs of chips at 75% more expensive than pretzels

    # Calculate the total cost of Maciek's purchases
    total_cost = pretzel_cost + chip_cost
    result = total_cost
    return result

print(solution())