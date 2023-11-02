def solution():
    
    cherry_pits = 80
    sprout_percentage = 0.25
    sprouted_pits = cherry_pits * sprout_percentage
    remaining_saplings = sprouted_pits - 6
    result = remaining_saplings
    return result

print(solution())