def solution():
    
    initial_students = 28
    final_students = 58
    students_added = final_students - initial_students
    percent_added = 40
    students_added_percent = students_added * (percent_added / 100)
    result = students_added_percent
    return result

print(solution())