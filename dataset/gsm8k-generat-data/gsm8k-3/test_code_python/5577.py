def solution():
    """How many cheese balls are in a 35oz barrel if the 24oz barrel has 60 servings and each serving has 12 cheese balls?"""
    # Calculate the total number of cheese balls in a 24oz barrel
    cheese_balls_24oz = 60 * 12

    # Calculate the ratio of cheese balls to ounces in the 24oz barrel
    ratio = cheese_balls_24oz / 24

    # Use the ratio to calculate the number of cheese balls in a 35oz barrel
    cheese_balls_35oz = ratio * 35

    # Display the number of cheese balls in the 35oz barrel
    result = cheese_balls_35oz
    return result

print(solution())