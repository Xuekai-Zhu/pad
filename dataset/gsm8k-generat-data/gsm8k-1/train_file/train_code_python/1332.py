def solution():
    """Louise is baking cakes for a gathering. She needs 60 cakes in total, and has already produced half this many. Today, she calculates how many cakes she has left to make and bakes half this amount. The next day, she again calculates how many cakes she has left to make and bakes a third of this amount. How many more cakes does Louise need to bake?"""
    total_cakes = 60
    cakes_already_baked = total_cakes / 2
    cakes_left_to_bake = total_cakes - cakes_already_baked
    cakes_baked_today = cakes_left_to_bake / 2
    cakes_left_to_bake = cakes_left_to_bake - cakes_baked_today
    cakes_baked_tomorrow = cakes_left_to_bake / 3
    total_cakes_baked = cakes_already_baked + cakes_baked_today + cakes_baked_tomorrow
    cakes_left_to_bake = total_cakes - total_cakes_baked
    result = cakes_left_to_bake
    return result

print(solution())