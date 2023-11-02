def solution():
    """There are 30 students in Ms. Leech's class. Twice as many girls as boys are in the class. There are 10 boys in the class and each boy today brought 5 cups for science activity class as Ms. Leech had instructed. If the total number of cups brought by the students in the class is 90, how many cups did each girl bring?"""
    # Define the number of boys and girls in the class
    boys = 10
    girls = 20

    # Calculate the total number of cups brought by the boys
    boy_cups = boys * 5

    # Calculate the total number of cups brought by the girls
    girl_cups = (90 - boy_cups) / girls

    # Display the number of cups brought by each girl
    result = girl_cups
    return result

print(solution())