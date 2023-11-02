def solution():
    members = 4
    slices_per_meal = 3
    meals_per_day = 2
    slices_per_day = members * slices_per_meal * meals_per_day
    slices_per_loaf = 12
    loaves_needed = slices_per_day / slices_per_loaf
    days_bread_lasts = 5 / loaves_needed
    result = days_bread_lasts
    return result

print(solution())