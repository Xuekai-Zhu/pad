def solution():
    # Calculate the total amount of fruit needed
    fruit_needed = (5 + 4 + 3) * 3  # 5 peach pies, 4 apple pies, and 3 blueberry pies, each using 3 pounds of fruit

    # Calculate the cost of the peaches
    peach_cost = 2.00 * (5 * 3)  # Each peach pie needs 3 pounds of peaches, which cost $2.00 per pound

    # Calculate the cost of the apples and blueberries
    apple_blueberry_cost = 1.00 * (4 * 3 + 3 * 3)  # 4 apple pies and 3 blueberry pies, each using 3 pounds of fruit, which are on sale for $1.00 per pound

    # Calculate the total cost of the fruit
    total_cost = peach_cost + apple_blueberry_cost
    result = total_cost
    return result

print(solution())