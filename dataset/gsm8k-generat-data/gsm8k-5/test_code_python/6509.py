def solution():
    turtle_weight = 30  # Sylvie has 30 pounds of turtles
    food_ratio = 1 / 0.5  # Each turtle needs 1 ounce of food per 1/2 pound of body weight
    total_food_needed = turtle_weight * food_ratio  # Total food needed for the turtles
    jars_of_food = total_food_needed / 15  # Total number of jars of food needed
    cost_per_jar = 2  # Each jar of food costs $2
    total_cost = jars_of_food * cost_per_jar  # Total cost of feeding the turtles
    result = total_cost
    return result

print(solution())