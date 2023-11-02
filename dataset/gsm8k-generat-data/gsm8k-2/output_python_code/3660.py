def solution():
    """Gabby planted a watermelon vine, a peach tree, and two plum trees in the spring. Over the summer, the plants grew and produced fruit. She only got one watermelon to grow, but she got twelve more peaches than that, and three times that number of plums. How many pieces of fruit did Gabby get to pick that summer?"""
    watermelon = 1
    peaches = watermelon + 12
    plums = 3 * watermelon
    total_fruit = watermelon + peaches + (2 * plums)
    result = total_fruit
    return result

print(solution())