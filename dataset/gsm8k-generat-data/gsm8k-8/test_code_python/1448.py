def solution():
    # Calculate the number of students with 5 notebooks
    num_students_with_5_notebooks = 28 // 2

    # Calculate the total number of notebooks for those students
    total_notebooks_for_5_students = num_students_with_5_notebooks * 5

    # Calculate the number of students with 3 notebooks
    num_students_with_3_notebooks = 28 - num_students_with_5_notebooks

    # Calculate the total number of notebooks for those students
    total_notebooks_for_3_students = num_students_with_3_notebooks * 3

    # Calculate the total number of notebooks in the classroom
    total_notebooks = total_notebooks_for_5_students + total_notebooks_for_3_students

    result = total_notebooks
    return result

print(solution())