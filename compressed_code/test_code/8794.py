def solution():
    
    muffins_per_recipe = 6
    students = 24
    muffins_needed = students * 1  
    batches_needed = muffins_needed // muffins_per_recipe
    months = 9
    batches_made = batches_needed * months
    result = batches_made
    return result

print(solution())