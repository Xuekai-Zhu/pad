def solution():
    weight_per_turtle = 0.5
    ounces_per_turtle = 1
    total_turtle_weight = 30

    # Calculate the total number of turtles
    total_turtles = total_turtle_weight / weight_per_turtle

    # Calculate the total amount of food needed in ounces
    total_food_needed = total_turtles * ounces_per_turtle

    # Calculate the total number of jars needed
    total_jars_needed = total_food_needed / 15

    # Calculate the total cost of all jars of food
    total_cost = total_jars_needed * 2
    result = total_cost
    return result

print(solution())