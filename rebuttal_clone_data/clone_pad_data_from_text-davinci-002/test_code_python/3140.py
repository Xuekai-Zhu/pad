def solution():
    chairs_per_row = 15
    rows = 10
    awardees = 1
    administrators = 2
    teachers = 3
    parents = 2
    students = rows - awardees - administrators - teachers - parents
    occupied_student_chairs = int(students * 4/5)
    vacant_student_chairs = students - occupied_student_chairs
    vacant_chairs = vacant_student_chairs + parents
    result = vacant_chairs
    
    return result

print(solution())