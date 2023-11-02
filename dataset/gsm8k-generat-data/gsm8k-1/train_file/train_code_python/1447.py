def solution():
    """There are 28 students in a classroom. Half of them have 5 notebooks each and the other half have 3 notebooks each. How many notebooks in total are in the classroom?"""
    total_students = 28
    half_students = total_students / 2
    notebooks_half1 = half_students * 5
    notebooks_half2 = half_students * 3
    total_notebooks = notebooks_half1 + notebooks_half2
    result = total_notebooks
    return result

print(solution())