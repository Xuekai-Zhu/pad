def solution():
    
    annual_profit = 8000
    first_quarter_profit = 1500
    third_quarter_profit = 3000
    fourth_quarter_profit = 2000
    second_quarter_profit = annual_profit - first_quarter_profit - third_quarter_profit - fourth_quarter_profit
    result = second_quarter_profit
    return result

print(solution())