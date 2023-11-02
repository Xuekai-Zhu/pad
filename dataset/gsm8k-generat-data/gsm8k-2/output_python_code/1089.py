def solution():
    """Beth had 150 students in her 10th-grade class. The following year 30 more students join. In her final year, 15 students left. How many students did Beth have in her class at the end of her final year?"""
    initial_students = 150
    second_year_students = initial_students + 30
    final_year_students = second_year_students - 15
    result = final_year_students
    return result

print(solution())