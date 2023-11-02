def solution():
    """Jessa needs to make cupcakes for 3 fourth-grade classes that each have 30 students and a P.E. class with 50 students. How many cupcakes does she need to make?"""
    # Define the number of students in each fourth-grade class and in the P.E. class
    fourth_grade_students = 30
    pe_students = 50

    # Calculate the total number of cupcakes needed
    total_cupcakes = (fourth_grade_students * 3) + pe_students

    # return the result
    result = total_cupcakes
    return result

print(solution())