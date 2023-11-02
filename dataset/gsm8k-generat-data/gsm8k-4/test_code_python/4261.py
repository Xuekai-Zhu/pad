def solution():
    """There are 30 students in Ms. Leech's class. Twice as many girls as boys are in the class. There are 10 boys in the class and each boy today brought 5 cups for science activity class as Ms. Leech had instructed. If the total number of cups brought by the students in the class is 90, how many cups did each girl bring?"""
    # Define the total number of students and the number of boys
    total_students = 30
    num_boys = 10

    # Calculate the number of girls in the class
    num_girls = 2 * num_boys

    # Calculate the total number of cups brought by the boys
    boys_cups = num_boys * 5

    # Calculate the total number of cups brought by all the students
    total_cups = 90

    # Calculate the total number of cups brought by the girls
    girls_cups = total_cups - boys_cups

    # Calculate the number of cups each girl brought
    cups_per_girl = girls_cups / num_girls

    #return the result
    result = cups_per_girl
    return result

print(solution())