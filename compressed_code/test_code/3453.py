def solution():
    
    loaves_per_recipe = 3
    total_loaves = 99
    bananas_per_recipe = 1
    total_bananas = (total_loaves // loaves_per_recipe) * bananas_per_recipe
    result = total_bananas
    return result

print(solution())