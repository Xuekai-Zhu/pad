def solution():
    serving_size = 12
    servings_per_24oz = 60
    ounces_in_24oz = 24
    ounces_in_35oz = 35

    cheese_balls_per_serving = serving_size
    servings_in_35oz = servings_per_24oz * (ounces_in_35oz / ounces_in_24oz)

    total_cheese_balls = servings_in_35oz * cheese_balls_per_serving
    result = total_cheese_balls
    return result

print(solution())