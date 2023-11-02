def solution():
    num_bananas = 5
    banana_cost = 2.0

    num_oranges = 10
    orange_cost = 1.5

    # Calculate the total cost of all bananas
    total_banana_cost = num_bananas * banana_cost

    # Calculate the total cost of all oranges
    total_orange_cost = num_oranges * orange_cost

    # Calculate the total cost of all fruits
    total_cost = total_banana_cost + total_orange_cost
    result = total_cost
    return result

print(solution())