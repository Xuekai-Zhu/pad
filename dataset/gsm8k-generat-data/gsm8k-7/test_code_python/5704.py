def solution():
    total_cost = 42
    banana_cost = 12
    bread_cost = 9
    milk_cost = 7

    # Calculate the total cost of all the groceries except the apples
    total_cost_without_apples = banana_cost + bread_cost + milk_cost

    # Calculate the cost of the apples
    apple_cost = total_cost - total_cost_without_apples
    result = apple_cost
    return result

print(solution())