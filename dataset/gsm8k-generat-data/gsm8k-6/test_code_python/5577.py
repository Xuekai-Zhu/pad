def solution():
    # Calculate the number of servings in a 35oz barrel
    servings_35oz = (35/24) * 60

    # Calculate the number of cheese balls in a 35oz barrel
    cheese_balls_35oz = servings_35oz * 12
    result = cheese_balls_35oz
    return result

print(solution())