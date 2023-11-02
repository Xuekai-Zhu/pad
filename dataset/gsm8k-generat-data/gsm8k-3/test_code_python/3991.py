def solution():
    """A public official wants to donate 5 new soccer balls per each class in two schools. Each school has 4 elementary school classes and 5 middle school classes.  How many soccer balls would the public official donate in all?"""
    # Define the number of classes and soccer balls per class
    CLASSES_PER_SCHOOL = 4 + 5
    SOCCER_BALLS_PER_CLASS = 5

    # Calculate the total number of soccer balls donated
    total_soccer_balls = CLASSES_PER_SCHOOL * 2 * SOCCER_BALLS_PER_CLASS

    # Display the total number of soccer balls donated
    result = total_soccer_balls
    return result

print(solution())