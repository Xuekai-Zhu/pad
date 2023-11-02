def solution():
    # Calculate the total cost of Olivia's groceries
    total_cost = 42

    # Calculate the cost of bananas, bread, and milk
    bananas_cost = 12
    bread_cost = 9
    milk_cost = 7

    # Calculate the total cost of bananas, bread, and milk
    total_bananas_bread_milk_cost = bananas_cost + bread_cost + milk_cost

    # Calculate the cost of apples
    apples_cost = total_cost - total_bananas_bread_milk_cost
    result = apples_cost
    return result

print(solution())