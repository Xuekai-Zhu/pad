def solution():
    initial_weight = 36
    eaten_weight = 6
    remaining_weight = initial_weight - eaten_weight
    num_piles = 3
    
    # Calculate the weight of each pile
    pile_weight = remaining_weight / num_piles
    result = pile_weight
    return result

print(solution())