def solution():
    # Calculate the total amount of food needed to feed the turtles
    total_food = 30 * 2  # each pound of turtle needs 2 ounces of food

    # Calculate the total number of jars of food needed
    total_jars = total_food / 15

    # Calculate the total cost of the food
    total_cost = total_jars * 2  # each jar costs $2

    result = total_cost
    return result

print(solution())