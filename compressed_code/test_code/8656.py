def solution():
    
    shoes_per_set = 3
    sets_needed = 5
    total_shoes_needed = (sets_needed * shoes_per_set) - 3  
    pairs_needed = (total_shoes_needed + 1) // 2  
    result = pairs_needed
    return result

print(solution())