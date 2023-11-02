def solution():
    """Jessa needs to make cupcakes for 3 fourth-grade classes that each have 30 students and a P.E. class with 50 students. How many cupcakes does she need to make?"""
    # Define the number of students in each fourth-grade class and in P.E.
    fourth_grade_students = 30
    pe_students = 50

    # Calculate the total number of cupcakes needed
    total_students = fourth_grade_students * 3 + pe_students
    cupcakes_needed = total_students * 1.5

    # Return the result
    result = cupcakes_needed
    return result

print(solution())