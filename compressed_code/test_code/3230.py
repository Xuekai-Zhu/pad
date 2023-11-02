def solution():
    
    can_weight = 2
    bottle_weight = 6
    max_weight = 100
    total_weight = 20 * can_weight
    bottles = (max_weight - total_weight) // bottle_weight
    total_money = bottles * 10 + 20 * 3
    result = total_money
    return result

print(solution())