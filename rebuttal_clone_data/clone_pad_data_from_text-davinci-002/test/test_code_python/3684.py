def solution():
    bananas_per_loaf = 4
    loaves_made_on_monday = 3
    loaves_made_on_tuesday = 2 * loaves_made_on_monday
    total_loaves = loaves_made_on_monday + loaves_made_on_tuesday
    total_bananas = bananas_per_loaf * total_loaves
    result = total_bananas
    return result

print(solution())