def solution():
    total_cost = 42  # The total cost of Olivia's groceries is $42
    bananas_cost = 12  # Olivia spent $12 on bananas
    bread_cost = 9  # Olivia spent $9 on bread
    milk_cost = 7  # Olivia spent $7 on milk

    # Calculate the cost of the apples
    apples_cost = total_cost - bananas_cost - bread_cost - milk_cost
    result = apples_cost
    return result

print(solution())