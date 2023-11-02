def solution():
    
    total_toys = 120
    larger_pile_ratio = 2
    smaller_pile_ratio = 1
    total_ratio = larger_pile_ratio + smaller_pile_ratio
    larger_pile = total_toys * larger_pile_ratio / total_ratio
    result = larger_pile
    return result

print(solution())