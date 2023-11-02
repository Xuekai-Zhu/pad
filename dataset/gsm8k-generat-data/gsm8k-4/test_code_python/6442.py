def solution():
    """Hot dog buns come in packages of 8. For the school picnic, Mr. Gates bought 30 packages of hot dog buns. He has four classes with 30 students in each class. How many hot dog buns can each of Mr. Gates' students get?"""
    # Define the number of hot dog bun packages
    num_packages = 30

    # Find the total number of hot dog buns
    total_buns = num_packages * 8

    # Define the number of classes and students per class
    num_classes = 4
    num_students_per_class = 30

    # Calculate the number of hot dog buns per student
    buns_per_student = total_buns / (num_classes * num_students_per_class)

    # Round down to the nearest whole number
    buns_per_student = int(buns_per_student)

    # return the result
    result = buns_per_student
    return result

print(solution())