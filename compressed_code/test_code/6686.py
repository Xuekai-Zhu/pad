def solution():
    
    total_profit = 1200
    mon_profit = total_profit / 3
    tue_profit = total_profit / 4
    wed_profit = total_profit - mon_profit - tue_profit
    result = wed_profit
    return result

print(solution())