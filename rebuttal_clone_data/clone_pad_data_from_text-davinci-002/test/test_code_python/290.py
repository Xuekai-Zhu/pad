def solution():
    lettuce_calories = 30
    cucumber_calories = 80
    crouton_calories = 20
    croutons_per_salad = 12
    salad_calories = lettuce_calories + cucumber_calories + (croutons_per_salad * crouton_calories)
    result = salad_calories
    return result

print(solution())