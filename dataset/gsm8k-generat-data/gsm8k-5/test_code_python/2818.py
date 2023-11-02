def solution():
    science_marks = 70
    music_marks = 80
    social_studies_marks = 85
    physics_marks = music_marks / 2  # Teresa scored half as many marks in physics as she scored in music

    # Calculate the total marks scored by Teresa in all the subjects
    total_marks = science_marks + music_marks + social_studies_marks + physics_marks
    result = total_marks
    return result

print(solution())