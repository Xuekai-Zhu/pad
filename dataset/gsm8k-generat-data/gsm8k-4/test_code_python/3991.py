def solution():
    """A public official wants to donate 5 new soccer balls per each class in two schools. Each school has 4 elementary school classes and 5 middle school classes.  How many soccer balls would the public official donate in all?"""
    # Define the number of classes per school
    CLASSES_PER_SCHOOL = 9

    # Define the number of soccer balls per class
    SOCCER_BALLS_PER_CLASS = 5

    # Calculate the total number of soccer balls to donate in both schools
    total_soccer_balls = CLASSES_PER_SCHOOL * SOCCER_BALLS_PER_CLASS * 2

    # return the result
    result = total_soccer_balls
    return result

print(solution())