def solution():
    """Sylvie is feeding her turtles. Each turtle needs 1 ounce of food per 1/2 pound of body weight. She has 30 pounds of turtles. Each jar of food contains 15 ounces and costs $2. How much does it cost to feed the turtles?"""
    turtle_weight = 30 # in pounds
    food_per_weight = 1/2 # in ounces
    total_food = turtle_weight * (food_per_weight*16) # in ounces
    jars_needed = total_food / 15
    cost_per_jar = 2 # in dollars
    total_cost = jars_needed * cost_per_jar
    result = total_cost
    return result

print(solution())