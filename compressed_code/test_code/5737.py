def solution():
    
    b_profit = 60000
    b_percent = 0.4
    a_percent = 0.6
    total_profit = b_profit / b_percent
    a_profit = total_profit * a_percent
    result = a_profit
    return result

print(solution())