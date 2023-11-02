def solution():
    total_students = 123
    students_attending_solo = 3
    total_couples = (total_students - students_attending_solo) / 2
    result = total_couples
    return result

print(solution())