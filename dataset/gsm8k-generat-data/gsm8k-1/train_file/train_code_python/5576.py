def solution():
    """How many cheese balls are in a 35oz barrel if the 24oz barrel has 60 servings and each serving has 12 cheese balls?"""
    cheese_balls_per_serving = 12
    servings_per_24oz_barrel = 60
    cheese_balls_per_24oz_barrel = cheese_balls_per_serving * servings_per_24oz_barrel
    oz_per_24oz_barrel = 24
    oz_per_35oz_barrel = 35
    cheese_balls_per_oz = cheese_balls_per_24oz_barrel / oz_per_24oz_barrel
    cheese_balls_in_35oz_barrel = cheese_balls_per_oz * oz_per_35oz_barrel
    result = cheese_balls_in_35oz_barrel
    return result

print(solution())