def solution():
    
    initial_weight = 36
    eaten_weight = 6
    remaining_weight = initial_weight - eaten_weight
    piles = 3
    weight_per_pile = remaining_weight / piles
    result = weight_per_pile
    return result

print(solution())