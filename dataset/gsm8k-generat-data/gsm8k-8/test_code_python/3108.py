def solution():
    money = 120
    hamburger_cost = 4
    milkshake_cost = 3
    
    # Calculate the cost of 8 hamburgers and 6 milkshakes
    total_cost = (8 * hamburger_cost) + (6 * milkshake_cost)
    
    # Calculate the remaining amount of money
    remaining_money = money - total_cost
    result = remaining_money
    return result

print(solution())