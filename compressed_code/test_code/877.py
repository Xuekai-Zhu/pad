def solution():
    
    total_profit = 1200
    monday_profit = total_profit / 3
    tuesday_profit = total_profit / 4
    wednesday_profit = total_profit - monday_profit - tuesday_profit
    result = wednesday_profit
    return result

print(solution())