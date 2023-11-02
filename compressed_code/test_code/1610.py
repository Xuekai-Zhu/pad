def solution():
    
    initial_weight = 36
    eaten_weight = 6
    remaining_weight = initial_weight - eaten_weight
    pile_weight = remaining_weight / 3
    result = pile_weight
    return result

print(solution())