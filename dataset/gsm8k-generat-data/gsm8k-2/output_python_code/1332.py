def solution():
    """Louise is baking cakes for a gathering. She needs 60 cakes in total, and has already produced half this many. Today, she calculates how many cakes she has left to make and bakes half this amount. The next day, she again calculates how many cakes she has left to make and bakes a third of this amount. How many more cakes does Louise need to bake?"""
    total_cakes = 60
    cakes_made = total_cakes / 2
    cakes_left = total_cakes - cakes_made
    first_day_cakes = cakes_left / 2
    cakes_left = cakes_left - first_day_cakes
    second_day_cakes = cakes_left / 3
    total_cakes_needed = cakes_made + first_day_cakes + second_day_cakes
    more_cakes_needed = total_cakes - total_cakes_needed
    result = more_cakes_needed
    return result

print(solution())