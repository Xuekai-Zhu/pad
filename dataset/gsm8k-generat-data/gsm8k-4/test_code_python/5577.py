def solution():
    """How many cheese balls are in a 35oz barrel if the 24oz barrel has 60 servings and each serving has 12 cheese balls?"""
    # Define the amount of cheese balls in a serving
    balls_per_serving = 12

    # Define the size of the 24oz barrel and the number of servings it contains
    size_24oz = 24
    servings_24oz = 60

    # Calculate the total number of cheese balls in the 24oz barrel
    balls_24oz = balls_per_serving * servings_24oz

    # Calculate the rate of cheese balls per ounce
    rate_balls_per_oz = balls_24oz / size_24oz

    # Calculate the number of cheese balls in a 35oz barrel
    balls_35oz = rate_balls_per_oz * 35

    result = balls_35oz
    return result

print(solution())