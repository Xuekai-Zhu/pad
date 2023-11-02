def solution():
    
    total_cost = (2 * 11) + (3 * 15) + (2 * 13)
    remaining_money = 50 - total_cost
    result = abs(remaining_money)
    return result

print(solution())