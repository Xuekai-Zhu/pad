def solution():
    
    num_sheep = 200
    wool_per_sheep = 10
    total_wool = num_sheep * wool_per_sheep
    price_per_pound = 20
    total_income = total_wool * price_per_pound
    expenses = 2000
    profit = total_income - expenses
    result = profit
    return result

print(solution())