def solution():
    slices_per_tomato = 8
    slices_per_meal = 20
    meals_needed = 8
    tomatoes_needed = (slices_per_meal * meals_needed) / slices_per_tomato
    result = tomatoes_needed
    return result

print(solution())