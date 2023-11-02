def solution():
    """There are 400 students. 120 students take dance as their elective. 200 students take art as their elective. The rest take music. What percentage of students take music?"""
    # Define the total number of students and the number of students in dance and art
    total_students = 400
    dance_students = 120
    art_students = 200

    # Calculate the number of students in music
    music_students = total_students - dance_students - art_students

    # Calculate the percentage of students in music
    music_percentage = (music_students / total_students) * 100

    # Display the percentage of students in music
    result = music_percentage
    return result

print(solution())