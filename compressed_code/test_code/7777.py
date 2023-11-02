def solution():
    
    savings = 50 + 37 + 11
    if savings > 75:
        savings += 25
    total_spent = 87
    money_left = savings - total_spent
    result = money_left
    return result

print(solution())