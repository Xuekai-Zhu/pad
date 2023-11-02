def solution():
    pieces_per_student = 4
    students = 40
    absent_students = 3
    present_students = students - absent_students
    pieces_needed = present_students * pieces_per_student
    result = pieces_needed
    return result

print(solution())