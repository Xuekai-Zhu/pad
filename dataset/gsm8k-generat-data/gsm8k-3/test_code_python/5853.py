def solution():
    """In a fruit salad, there are raspberries, green grapes, and red grapes. There are seven more than 3 times the number of red grapes as green grapes. There are 5 less raspberries than green grapes. If there are 102 pieces of fruit in the salad, how many red grapes are in the salad?"""
    # Define the variables
    green_grapes = 0
    red_grapes = 0
    raspberries = 0

    # Define the equations
    red_grapes = (7 + 3 * green_grapes)
    raspberries = (green_grapes - 5)
    total_fruit = (green_grapes + red_grapes + raspberries)

    # Define the conditions
    while total_fruit != 102:
        if total_fruit < 102:
            green_grapes += 1
        else:
            green_grapes -= 1
        red_grapes = (7 + 3 * green_grapes)
        raspberries = (green_grapes - 5)
        total_fruit = (green_grapes + red_grapes + raspberries)

    # Display the number of red grapes
    result = red_grapes
    return result

print(solution())