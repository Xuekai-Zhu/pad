def solution():
    """There were 28 students inside a bus before stopping at an intersection. After stopping at an intersection,
    there were 58 students on the bus. What's 40% of the number of students who entered the bus at the intermediate stop?"""
    initial_students = 28
    final_students = 58
    students_added = final_students - initial_students
    percent_added = 40
    students_added_percent = students_added * (percent_added / 100)
    result = students_added_percent
    return result

print(solution())