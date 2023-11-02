def solution():
    
    total_cost = (1.5 * 6) + 3 + 2.5 + (4 * 0.75) + (2 * 2) + 2.5
    if total_cost >= 35:
        result = 0
    else:
        result = 35 - total_cost
    return result

print(solution())