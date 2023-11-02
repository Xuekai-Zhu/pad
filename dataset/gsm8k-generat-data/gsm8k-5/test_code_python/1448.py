def solution():
    total_students = 28  # There are 28 students in the classroom

    # Half of them have 5 notebooks each
    half_1 = total_students // 2
    notebooks_1 = 5 * half_1

    # The other half have 3 notebooks each
    half_2 = total_students - half_1
    notebooks_2 = 3 * half_2

    # Total number of notebooks in the classroom
    total_notebooks = notebooks_1 + notebooks_2
    result = total_notebooks
    return result

print(solution())