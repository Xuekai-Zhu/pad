def solution():
    students = 240
    students_reading_novels = (1/6 * students) + (35/100 * students) + (5/12 * students)
    students_not_reading_novels = students - students_reading_novels
    result = students_not_reading_novels
    
    return result

print(solution())