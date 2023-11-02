def solution():
    # Calculate the cost of each type of fruit
    banana_cost = 1 * 4
    apple_cost = 2 * 3
    strawberry_cost = (4 / 12) * 24
    avocado_cost = 3 * 2
    grape_cost = 2 * 2

    # Calculate the total cost of the fruit basket
    total_cost = banana_cost + apple_cost + strawberry_cost + avocado_cost + grape_cost
    result = total_cost
    return result

print(solution())