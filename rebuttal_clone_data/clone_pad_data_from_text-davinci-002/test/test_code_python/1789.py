def solution():
    total_students = 400
    students_taking_dance = 120
    students_taking_art = 200
    students_taking_music = total_students - students_taking_dance - students_taking_art
    percent_taking_music = students_taking_music / total_students * 100
    result = percent_taking_music
    
    return result

print(solution())