def solution():
    total_students = 30  # There are 30 students in Ms. Leech's class
    boys = 10  # There are 10 boys in the class
    girls = 2 * boys  # There are twice as many girls as boys in the class

    boys_cups = boys * 5  # Each boy brought 5 cups
    total_cups = boys_cups + girls * x  # The total number of cups is 90

    # Solve for x to find how many cups each girl brought
    x = (90 - boys_cups) / girls
    result = x
    return result

print(solution())