def solution():
    # Calculate the total cost of purchasing fruit for the pies
    peach_cost = 5 * 3 * 2  # 5 peach pies, 3 pounds of peaches each, at $2.00 per pound
    apple_cost = 4 * 3 * 1  # 4 apple pies, 3 pounds of apples each, at $1.00 per pound
    blueberry_cost = 3 * 3 * 1  # 3 blueberry pies, 3 pounds of blueberries each, at $1.00 per pound
    total_cost = peach_cost + apple_cost + blueberry_cost
    result = total_cost
    return result

print(solution())