def solution():
    # Calculate the total cost of food bought by Lyra
    total_cost = 12 + 5*3  # 1 bucket of fried chicken costs $12, 5 pounds of beef cost $3 per pound

    # Calculate the amount left on Lyra's budget
    budget_left = 80 - total_cost
    result = budget_left
    return result

print(solution())