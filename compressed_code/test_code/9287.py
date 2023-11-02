def solution():
    
    loaves_per_recipe = 3
    total_loaves = 99
    bananas_per_recipe = 1
    bananas_needed = (total_loaves / loaves_per_recipe) * bananas_per_recipe
    result = bananas_needed
    return result

print(solution())