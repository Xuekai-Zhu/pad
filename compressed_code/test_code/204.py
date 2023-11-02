def solution():
    
    savings = [2, 4, 8]
    for i in range(3, 6):
        savings.append(savings[i-1] * 2)
    total_savings = sum(savings)
    result = total_savings
    return result

print(solution())