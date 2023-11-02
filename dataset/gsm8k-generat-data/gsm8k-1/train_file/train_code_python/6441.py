def solution():
    """Hot dog buns come in packages of 8. For the school picnic, Mr. Gates bought 30 packages of hot dog buns. He has four classes with 30 students in each class. How many hot dog buns can each of Mr. Gates' students get?"""
    buns_per_package = 8
    total_buns = 30 * buns_per_package
    total_students = 4 * 30
    buns_per_student = total_buns // total_students
    result = buns_per_student
    return result

print(solution())