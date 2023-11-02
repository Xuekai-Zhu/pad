def solution():
    
    weeks = [4, 4, 4]
    amounts = [5, 10, 20]
    total_savings = 0
    for i in range(len(weeks)):
        total_savings += weeks[i] * amounts[i]
    result = total_savings
    return result

print(solution())