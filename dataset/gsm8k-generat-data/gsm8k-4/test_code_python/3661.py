def solution():
    """Gabby planted a watermelon vine, a peach tree, and two plum trees in the spring. Over the summer, the plants grew and produced fruit. She only got one watermelon to grow, but she got twelve more peaches than that, and three times that number of plums. How many pieces of fruit did Gabby get to pick that summer?"""
    # Define the initial number of each plant
    watermelon = 1
    peach_tree = 1
    plum_trees = 2

    # Calculate the number of peaches and plums produced
    peaches = watermelon + 12
    plums = 3 * peaches

    # Calculate the total number of fruit
    total_fruit = watermelon + peaches + plums

    # return the result
    result = total_fruit
    return result

print(solution())