def solution():
    """Jason is making a salad. The lettuce has 30 calories, the cucumber has 80 calories, and the 12 croutons have 20 calories each. How many calories are in the salad?"""
    lettuce_calories = 30
    cucumber_calories = 80
    crouton_calories = 20
    crouton_count = 12
    total_calories = lettuce_calories + cucumber_calories + (crouton_calories * crouton_count)
    result = total_calories
    return result

print(solution())