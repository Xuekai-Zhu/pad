def solution():
    """Sylvie is feeding her turtles. Each turtle needs 1 ounce of food per 1/2 pound of body weight. She has 30 pounds of turtles. Each jar of food contains 15 ounces and costs $2. How much does it cost to feed the turtles?"""
    # Define the amount of food needed for each turtle
    food_per_turtle = 1 / 0.5

    # Calculate the total amount of food needed for all the turtles
    total_food = food_per_turtle * 30

    # Calculate the number of jars of food needed
    jars_of_food = total_food / 15

    # Calculate the cost of the jars of food
    cost = jars_of_food * 2

    # return the result
    result = cost
    return result

print(solution())