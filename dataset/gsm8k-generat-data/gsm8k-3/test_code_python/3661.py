def solution():
    """Gabby planted a watermelon vine, a peach tree, and two plum trees in the spring. Over the summer, the plants grew and produced fruit. She only got one watermelon to grow, but she got twelve more peaches than that, and three times that number of plums. How many pieces of fruit did Gabby get to pick that summer?"""
    # Define the number of watermelons, peaches, and plums
    watermelons = 1
    peaches = watermelons + 12
    plums = 3 * watermelons

    # Calculate the total number of pieces of fruit
    total_fruit = watermelons + peaches + (2 * plums)

    # Display the total number of pieces of fruit
    result = total_fruit
    return result

print(solution())