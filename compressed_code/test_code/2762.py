def solution():
    
    savings = 21 + 46 + 45
    expenses = 12 + 54
    total = savings - expenses

    if total > 125:
        total += 25

    result = total
    return result

print(solution())