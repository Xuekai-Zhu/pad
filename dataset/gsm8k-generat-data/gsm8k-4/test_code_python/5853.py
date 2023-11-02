def solution():
    """In a fruit salad, there are raspberries, green grapes, and red grapes. There are seven more than 3 times the number of red grapes as green grapes. There are 5 less raspberries than green grapes. If there are 102 pieces of fruit in the salad, how many red grapes are in the salad?"""
    # Define the variables
    red_grapes = None
    green_grapes = None
    raspberries = None

    # Set up the equations
    red_grapes = (7 + 3*green_grapes)
    raspberries = (green_grapes - 5)
    total_fruit = (red_grapes + green_grapes + raspberries)

    # Solve for green grapes
    for i in range(1, 103):
        green_grapes = i
        if (red_grapes == 7 + 3*green_grapes) and (raspberries == green_grapes - 5) and (total_fruit == 102):
            break

    # Solve for red grapes
    red_grapes = 7 + 3*green_grapes

    # return the result
    result = red_grapes
    return result

print(solution())