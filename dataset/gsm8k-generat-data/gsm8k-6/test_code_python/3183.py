def solution():
    # Calculate the number of students taking music as their elective
    music_students = 400 - 120 - 200  # the rest of the students take music 

    # Calculate the percentage of students taking music
    music_percentage = (music_students / 400) * 100

    result = music_percentage
    return result

print(solution())