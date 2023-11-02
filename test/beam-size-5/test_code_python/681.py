def solution():
    apple_weight = 1
    apple_price = 4

    banana_weight = 2
    banana_price = 2

    orange_weight = 2
    orange_price = 3

    # Calculate the total cost of apples
    apple_cost = apple_weight * apple_price

    # Calculate the total cost of bananas
    banana_cost = banana_weight * banana_price

    # Calculate the total cost of oranges
    orange_cost = orange_weight * orange_price

    # Calculate the total cost of all items
    total_cost = apple_cost + banana_cost + orange_cost
    result = total_cost
    return result

print(solution())