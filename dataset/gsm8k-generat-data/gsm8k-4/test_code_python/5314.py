def solution():
    """A coach placed 15 tennis balls and 5 soccer balls each into 5 baskets. He gave 5 of his students a short period of time to remove as many balls each from a basket as they could. 3 of them removed 8 balls each and the other 2 removed a certain number of balls each. If a total of 56 balls are still in the baskets, how many balls did the other 2 students each remove?"""
    # Define the initial number of tennis and soccer balls in each basket
    TENNIS_BALLS = 15
    SOCCER_BALLS = 5

    # Define the number of baskets
    BASKETS = 5

    # Define the total number of balls in each basket
    TOTAL_BALLS = TENNIS_BALLS + SOCCER_BALLS

    # Define the number of balls removed by the first 3 students
    BALLS_REMOVED_3 = 3 * 8

    # Calculate the total number of balls removed by all 5 students
    total_balls_removed = BALLS_REMOVED_3 + (2 * x)

    # Calculate the total number of balls remaining in the baskets
    total_balls_remaining = (BASKETS * TOTAL_BALLS) - total_balls_removed

    # Calculate the number of balls removed by the other 2 students
    x = (total_balls_remaining - BALLS_REMOVED_3) / 2

    # return the result
    result = x
    return result

print(solution())