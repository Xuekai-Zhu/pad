def solution():
    
    total_students = 400
    dance_students = 120
    art_students = 200
    music_students = total_students - dance_students - art_students
    music_percent = (music_students / total_students) * 100
    result = music_percent
    return result

print(solution())