def solution():
    
    savings = 21 + 46 + 45
    expenses = 12 + 54
    total_money = savings - expenses
    if total_money > 125:
        total_money += 25
    result = total_money
    return result

print(solution())