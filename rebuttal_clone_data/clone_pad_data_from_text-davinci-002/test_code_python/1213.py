def solution():
    
    total_items = 75
    lyssa_incorrect = total_items * 0.2
    precious_incorrect = 12
    lyssa_correct = total_items - lyssa_incorrect
    precious_correct = total_items - precious_incorrect
    
    difference = lyssa_correct - precious_correct
    result = difference
    return result

print(solution())