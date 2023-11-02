def solution():
    """The batting cage sells golf balls by the dozen. They charge $30 for 3 dozen. Dan buys 5 dozen, Gus buys 2 dozen, and Chris buys 48 golf balls. How many golf balls do they purchase in total, assuming 12 golf balls are 1 dozen?"""
    # Define the number of golf balls per dozen and the cost for 3 dozen
    GOLF_BALLS_PER_DOZEN = 12
    COST_FOR_3_DOZEN = 30

    # Define the number of dozens purchased by each person
    dan_dozens = 5
    gus_dozens = 2

    # Calculate the number of golf balls purchased by each person
    dan_golf_balls = dan_dozens * GOLF_BALLS_PER_DOZEN
    gus_golf_balls = gus_dozens * GOLF_BALLS_PER_DOZEN
    chris_golf_balls = 48

    # Calculate the total number of golf balls purchased
    total_golf_balls = dan_golf_balls + gus_golf_balls + chris_golf_balls

    # Display the total number of golf balls purchased
    result = total_golf_balls
    return result

print(solution())