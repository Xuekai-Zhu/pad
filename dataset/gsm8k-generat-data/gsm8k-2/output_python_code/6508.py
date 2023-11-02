def solution():
    """Sylvie is feeding her turtles. Each turtle needs 1 ounce of food per 1/2 pound of body weight. She has 30 pounds of turtles. Each jar of food contains 15 ounces and costs $2. How much does it cost to feed the turtles?"""
    turtle_weight = 0.5
    food_per_turtle = 1
    total_weight = 30
    total_turtles = total_weight / turtle_weight
    total_food = total_turtles * food_per_turtle
    total_jars = (total_food / 15) + 1  # Adding 1 to account for partial jar
    cost_per_jar = 2
    total_cost = total_jars * cost_per_jar
    result = total_cost
    return result

print(solution())