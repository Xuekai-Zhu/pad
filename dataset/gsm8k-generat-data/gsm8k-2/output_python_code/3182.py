def solution():
    """There are 400 students. 120 students take dance as their elective. 200 students take art as their elective. The rest take music. What percentage of students take music?"""
    total_students = 400
    dance_students = 120
    art_students = 200
    music_students = total_students - dance_students - art_students
    music_percentage = 100 * (music_students / total_students)
    result = music_percentage
    return result

print(solution())