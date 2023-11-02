def solution():
    """Hot dog buns come in packages of 8. For the school picnic, Mr. Gates bought 30 packages of hot dog buns. He has four classes with 30 students in each class. How many hot dog buns can each of Mr. Gates' students get?"""
    # Calculate the total number of hot dog buns
    total_buns = 30 * 8

    # Calculate the number of students
    num_students = 4 * 30

    # Divide the total number of buns by the number of students to get the number of buns per student
    buns_per_student = total_buns // num_students

    # Display the number of hot dog buns per student
    result = buns_per_student
    return result

print(solution())