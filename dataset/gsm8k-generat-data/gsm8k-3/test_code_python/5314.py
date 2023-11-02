def solution():
    """A coach placed 15 tennis balls and 5 soccer balls each into 5 baskets. He gave 5 of his students a short period of time to remove as many balls each from a basket as they could. 3 of them removed 8 balls each and the other 2 removed a certain number of balls each. If a total of 56 balls are still in the baskets, how many balls did the other 2 students each remove?"""
    # Define the number of tennis and soccer balls in each basket
    TENNIS_BALLS = 15
    SOCCER_BALLS = 5

    # Define the number of baskets and students
    BASKETS = 5
    STUDENTS = 5

    # Define the number of balls removed by the first 3 students
    balls_removed = 8

    # Calculate the total number of balls originally in the baskets
    total_balls = (TENNIS_BALLS + SOCCER_BALLS) * BASKETS

    # Subtract the balls removed by the first 3 students to get the number of balls remaining in the baskets
    remaining_balls = total_balls - (3 * balls_removed)

    # Subtract the remaining balls from the total to get the total number of balls removed by the other 2 students
    other_balls_removed = total_balls - remaining_balls - (2 * balls_removed)

    # Divide the other balls removed equally between the 2 students
    balls_each = other_balls_removed / 2

    # Display the number of balls each of the other 2 students removed
    result = balls_each
    return result

print(solution())