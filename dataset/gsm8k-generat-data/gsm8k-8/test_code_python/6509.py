def solution():
    # Calculate the total weight of the turtles
    total_weight = 30

    # Calculate the total amount of food needed
    total_food = total_weight * 2

    # Calculate the total amount of food in ounces
    total_food_ounces = total_food * 1

    # Calculate the total number of jars needed
    total_jars = total_food_ounces / 15

    # Calculate the total cost of the food
    total_cost = total_jars * 2

    result = total_cost
    return result

print(solution())