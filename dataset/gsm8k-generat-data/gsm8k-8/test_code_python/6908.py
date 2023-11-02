def solution():
    # Calculate James' new total and body weight
    old_total = 2200
    total_increase = old_total * 0.15
    new_total = old_total + total_increase
    old_weight = 245
    new_weight = old_weight + 8
    
    # Calculate the ratio of his lifting total to body weight
    ratio = new_total / new_weight
    result = ratio
    return result

print(solution())