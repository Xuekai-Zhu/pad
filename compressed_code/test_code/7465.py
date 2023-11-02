def solution():
    
    total_spent = (5 * 5) + (10 * 5) + (3 * 5)
    change = 200 - total_spent
    bags_can_buy = change // 10
    result = bags_can_buy
    return result

print(solution())