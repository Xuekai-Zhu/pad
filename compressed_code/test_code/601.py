def solution():
    
    total_appetizers_needed = 6 * 30
    appetizers_made = (3 + 2 + 2) * 12  
    appetizers_left_to_make = (total_appetizers_needed - appetizers_made) / 12  
    result = appetizers_left_to_make
    return result

print(solution())