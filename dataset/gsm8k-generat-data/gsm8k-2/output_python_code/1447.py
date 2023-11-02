def solution():
    """There are 28 students in a classroom. Half of them have 5 notebooks each and the other half have 3 notebooks each. How many notebooks in total are in the classroom?"""
    total_students = 28
    half_students = int(total_students / 2)
    half_with_5 = half_students * 5
    half_with_3 = half_students * 3
    total_notebooks = half_with_5 + half_with_3
    result = total_notebooks
    return result

print(solution())