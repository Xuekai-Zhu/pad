def solution():
    
    initial_weight = 8
    increase_percent = 50
    increase_amount = initial_weight * (increase_percent / 100)
    new_weight = initial_weight + increase_amount
    final_weight = new_weight + 2
    result = final_weight
    return result

print(solution())