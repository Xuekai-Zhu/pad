def solution():
    # Calculate the total cost of hamburgers and milkshakes
    hamburger_cost = 4 * 8
    milkshake_cost = 3 * 6
    total_cost = hamburger_cost + milkshake_cost
    
    # Calculate how much money Annie has left
    left_money = 120 - total_cost
    result = left_money
    return result

print(solution())