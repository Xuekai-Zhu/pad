def solution():
    total_students = 400
    dance_students = 120
    art_students = 200

    # Calculate the number of students who take music
    music_students = total_students - dance_students - art_students

    # Calculate the percentage of students who take music
    music_percentage = (music_students / total_students) * 100
    result = music_percentage
    return result

print(solution())