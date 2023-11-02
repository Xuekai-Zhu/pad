def solution():
    pieces_per_student = 4
    total_students = 40 // pieces_per_student
    absent_students = 3
    remaining_students = total_students - absent_students
    pieces_to_make = remaining_students * pieces_per_student
    result = pieces_to_make
    return result

print(solution())