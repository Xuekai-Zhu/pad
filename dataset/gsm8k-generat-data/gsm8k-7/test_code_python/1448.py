def solution():
    num_students = 28

    # Calculate the number of students with 5 notebooks
    num_students_5 = num_students / 2

    # Calculate the number of students with 3 notebooks
    num_students_3 = num_students / 2

    # Calculate the total number of notebooks with students with 5 notebooks
    total_notebooks_5 = num_students_5 * 5

    # Calculate the total number of notebooks with students with 3 notebooks
    total_notebooks_3 = num_students_3 * 3

    # Calculate the total number of notebooks in the classroom
    total_notebooks = total_notebooks_5 + total_notebooks_3
    result = total_notebooks
    return result

print(solution())