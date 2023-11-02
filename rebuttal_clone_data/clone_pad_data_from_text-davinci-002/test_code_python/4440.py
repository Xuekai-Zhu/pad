def solution():
    loaves_needed = 99
    loaves_per_recipe = 3
    bananas_per_loaf = 1
    total_bananas = loaves_needed * bananas_per_loaf / loaves_per_recipe
    result = total_bananas
    return result

print(solution())