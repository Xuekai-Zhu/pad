def solution():
    # Define the ingredients in a normal batch of chili
    chilis = 1
    beans = 2
    tomatoes = 1.5 * beans

    # Calculate the ingredients for a quadruple batch of chili
    chilis_quad = chilis * 4
    beans_quad = beans * 4 * 2
    tomatoes_quad = tomatoes * 4 * 1.5

    # Calculate the total cans of food needed
    total_cans = chilis_quad + beans_quad + tomatoes_quad
    result = total_cans
    return result

print(solution())