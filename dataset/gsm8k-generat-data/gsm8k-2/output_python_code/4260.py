def solution():
    """There are 30 students in Ms. Leech's class. Twice as many girls as boys are in the class. There are 10 boys in the class and each boy today brought 5 cups for science activity class as Ms. Leech had instructed. If the total number of cups brought by the students in the class is 90, how many cups did each girl bring?"""
    total_students = 30
    boys = 10
    girls = 2 * boys
    boy_cups = 5 * boys
    total_cups = 90
    girl_cups = (total_cups - boy_cups) / girls
    result = girl_cups
    return result

print(solution())