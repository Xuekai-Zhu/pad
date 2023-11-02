def solution():
    """In a classroom of 81 students, two-thirds are wearing striped shirts while the others are wearing checkered shirts.
    If there are 19 more students wearing shorts than checkered shirts, how many more students are wearing striped shirts than shorts?"""
    total_students = 81
    striped_shirts = (2/3) * total_students
    checkered_shirts = total_students - striped_shirts
    shorts = checkered_shirts + 19
    difference = striped_shirts - shorts
    result = difference
    return result

print(solution())