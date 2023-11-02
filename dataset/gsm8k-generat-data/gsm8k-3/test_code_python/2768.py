def solution():
    """Robert had 25 balls. Tim gave him half of his 40 balls. How many balls does Robert have now?"""
    # Define the initial number of balls Robert had
    robert_balls = 25

    # Define the number of balls Tim gave to Robert
    tim_balls = 40
    robert_balls += tim_balls / 2

    # Display the total number of balls Robert has now
    result = robert_balls
    return result

print(solution())