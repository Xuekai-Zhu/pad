def solution():
    
    total_scissors_cost = 8 * 5
    total_erasers_cost = 10 * 4
    total_cost = total_scissors_cost + total_erasers_cost
    remaining_money = 100 - total_cost
    result = remaining_money
    return result

print(solution())