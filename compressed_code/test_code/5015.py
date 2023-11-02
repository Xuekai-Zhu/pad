def solution():
    
    needed_flour = 6
    measuring_cup_size = 0.25
    total_flour = 8
    scoops_to_remove = (total_flour - needed_flour) // measuring_cup_size
    result = scoops_to_remove
    return result

print(solution())