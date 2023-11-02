def solution():
    total_students = 400  # Total number of students
    dance_students = 120  # Number of students taking dance as their elective
    art_students = 200  # Number of students taking art as their elective

    # Calculate the number of students taking music
    music_students = total_students - dance_students - art_students

    # Calculate the percentage of students taking music
    percentage_music = (music_students / total_students) * 100
    result = percentage_music
    return result

print(solution())