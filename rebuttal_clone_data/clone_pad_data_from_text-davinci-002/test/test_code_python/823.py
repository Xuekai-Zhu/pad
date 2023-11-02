def solution():
    total_students = 28
    students_with_5_notebooks = total_students / 2
    students_with_3_notebooks = total_students / 2
    notebooks_with_5_students = students_with_5_notebooks * 5
    notebooks_with_3_students = students_with_3_notebooks * 3
    total_notebooks = notebooks_with_5_students + notebooks_with_3_students 
    result = total_notebooks
    return result

print(solution())