def solution():
    """Jessa needs to make cupcakes for 3 fourth-grade classes that each have 30 students and a P.E. class with 50 students. How many cupcakes does she need to make?"""
    fourth_grade_students = 3 * 30
    pe_students = 50
    total_students = fourth_grade_students + pe_students
    cupcakes_per_student = 1
    total_cupcakes = total_students * cupcakes_per_student
    result = total_cupcakes
    return result

print(solution())