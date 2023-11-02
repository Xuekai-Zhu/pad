def solution():
    
    slices_per_day = (3 + 2) * 4
    slices_per_loaf = 12
    slices_per_five_loaves = slices_per_loaf * 5
    days = slices_per_five_loaves // slices_per_day
    result = days
    return result

print(solution())