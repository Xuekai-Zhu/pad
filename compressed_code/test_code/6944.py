def solution():
    
    bridge_capacity = 100
    kelly_weight = 34
    megan_weight = kelly_weight / 0.85
    mike_weight = megan_weight + 5
    total_weight = kelly_weight + megan_weight + mike_weight
    excess_weight = total_weight - bridge_capacity
    result = excess_weight
    return result

print(solution())