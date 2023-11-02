def solution():
    """How many cheese balls are in a 35oz barrel if the 24oz barrel has 60 servings and each serving has 12 cheese balls?"""
    servings_in_24oz = 60
    cheese_balls_per_serving = 12
    total_cheese_balls_in_24oz = servings_in_24oz * cheese_balls_per_serving
    ounces_in_35oz = 35
    ounces_in_24oz = 24
    cheese_balls_per_ounce = total_cheese_balls_in_24oz / ounces_in_24oz
    total_cheese_balls_in_35oz = cheese_balls_per_ounce * ounces_in_35oz
    result = total_cheese_balls_in_35oz
    return result

print(solution())