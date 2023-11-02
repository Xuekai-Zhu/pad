def solution():
    total_students = 20
    students_playing_basketball = total_students / 2
    students_playing_volleyball = total_students * 2 / 5
    students_playing_both = total_students / 10
    students_not_playing = total_students - (students_playing_basketball + students_playing_volleyball + students_playing_both)
    result = students_not_playing
    return result

print(solution())