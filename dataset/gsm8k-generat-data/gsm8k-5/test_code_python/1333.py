def solution():
    total_cakes = 60  # Louise needs 60 cakes in total
    cakes_already_made = total_cakes / 2  # Louise has already made half the total number of cakes
    cakes_left_to_make = total_cakes - cakes_already_made  # Louise still needs to make these many cakes

    # On the first day, Louise bakes half the remaining cakes
    cakes_left_to_make /= 2

    # On the second day, Louise bakes one-third of the remaining cakes
    cakes_left_to_make /= 3

    # Calculate the total number of cakes Louise needs to bake
    total_cakes_to_bake = total_cakes - cakes_already_made - cakes_left_to_make
    result = total_cakes_to_bake
    return result

print(solution())