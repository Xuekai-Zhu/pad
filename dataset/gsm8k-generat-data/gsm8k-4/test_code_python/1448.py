def solution():
    """There are 28 students in a classroom. Half of them have 5 notebooks each and the other half have 3 notebooks each. How many notebooks in total are in the classroom?"""
    # Define the number of students
    total_students = 28

    # Calculate the number of students with 5 notebooks
    students_with_5nb = total_students // 2

    # Calculate the number of students with 3 notebooks
    students_with_3nb = total_students - students_with_5nb

    # Calculate the total number of notebooks
    total_notebooks = (students_with_5nb * 5) + (students_with_3nb * 3)

    # return the result
    result = total_notebooks
    return result

print(solution())