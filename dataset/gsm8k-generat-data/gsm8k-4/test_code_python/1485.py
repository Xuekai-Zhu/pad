def solution():
    """Adam has 50 balls. 20 balls are red, 10 are blue, and the rest are either pink or orange. If there are 3 times as many pink as orange balls, how many orange balls are there?"""
    # Define the total number of balls and the number of red and blue balls
    total_balls = 50
    red_balls = 20
    blue_balls = 10

    # Calculate the number of pink balls
    pink_balls = total_balls - red_balls - blue_balls

    # Calculate the number of orange balls
    orange_balls = pink_balls / 4

    # Return the number of orange balls
    result = orange_balls
    return result

print(solution())