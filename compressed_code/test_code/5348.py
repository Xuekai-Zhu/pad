def solution():
    
    initial_total = 2200
    initial_weight = 245
    total_gain = 0.15 * initial_total
    final_total = initial_total + total_gain
    final_weight = initial_weight + 8
    ratio = final_total / final_weight
    result = ratio
    return result

print(solution())