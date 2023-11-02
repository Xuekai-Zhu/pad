def solution():
    """Adam has 50 balls. 20 balls are red, 10 are blue, and the rest are either pink or orange. If there are 3 times as many pink as orange balls, how many orange balls are there?"""
    # Define the number of red and blue balls
    red_balls = 20
    blue_balls = 10

    # Calculate the number of pink balls
    pink_balls = 3 * orange_balls

    # Calculate the total number of balls
    total_balls = red_balls + blue_balls + pink_balls + orange_balls

    # Use the total number of balls to solve for orange balls
    orange_balls = 50 - total_balls

    # Display the number of orange balls
    result = orange_balls
    return result

print(solution())