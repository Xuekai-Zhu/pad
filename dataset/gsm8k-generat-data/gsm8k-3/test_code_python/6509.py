def solution():
    """Sylvie is feeding her turtles. Each turtle needs 1 ounce of food per 1/2 pound of body weight. She has 30 pounds of turtles. Each jar of food contains 15 ounces and costs $2.  How much does it cost to feed the turtles?"""
    # Define the amount of food each turtle needs in ounces per pound of body weight
    FOOD_PER_POUND = 1

    # Define the total weight of the turtles in pounds
    total_weight = 30

    # Calculate the total amount of food needed in ounces
    total_food = total_weight * 2 * FOOD_PER_POUND

    # Calculate the number of jars of food needed
    jars_needed = int(total_food / 15) + 1

    # Calculate the total cost of the food
    total_cost = jars_needed * 2

    # Display the total cost
    result = total_cost
    return result

print(solution())