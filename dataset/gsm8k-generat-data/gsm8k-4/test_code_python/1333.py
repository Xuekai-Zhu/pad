def solution():
    """ Louise is baking cakes for a gathering. She needs 60 cakes in total, and has already produced half this many. Today, she calculates how many cakes she has left to make and bakes half this amount. The next day, she again calculates how many cakes she has left to make and bakes a third of this amount. How many more cakes does Louise need to bake? """
    # Define the total number of cakes needed
    total_cakes = 60

    # Calculate the number of cakes already produced
    produced_cakes = total_cakes / 2

    # Calculate the number of cakes left to make after the first bake
    cakes_left = total_cakes - produced_cakes
    half_cakes_left = cakes_left / 2

    # Calculate the number of cakes left to make after the second bake
    cakes_left = cakes_left - half_cakes_left
    third_cakes_left = cakes_left / 3

    # Calculate the total number of cakes Louise needs to bake
    total_bake = half_cakes_left + third_cakes_left

    result = total_bake

    return result

print(solution())