def solution():
    total_students = 24
    reading_students = total_students / 2
    playing_students = total_students / 3
    homework_students = total_students - reading_students - playing_students
    result = homework_students
    return result

print(solution())