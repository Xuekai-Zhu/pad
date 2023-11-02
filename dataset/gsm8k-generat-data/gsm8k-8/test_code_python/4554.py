def solution():
    # Calculate the total pounds of fruit needed
    total_fruit = (5 + 4 + 3) * 3

    # Calculate the cost of the peaches
    peach_cost = 2.00 * 3 * 5

    # Calculate the cost of the apples and blueberries
    apple_blueberry_cost = 1.00 * 3 * (4 + 3)

    # Calculate the total cost
    total_cost = peach_cost + apple_blueberry_cost
    result = total_cost
    return result

print(solution())