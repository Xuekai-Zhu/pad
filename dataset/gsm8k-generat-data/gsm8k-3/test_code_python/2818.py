def solution():
    """Teresa scored 70 marks in science, 80 in music, 85 in social studies, and the physics exam, which was the hardest test that Teresa had ever taken in her entire life, she scored half as many marks as she scored in music. Calculate the total marks Teresa scored in all the subjects."""
    # Define the marks obtained in each subject
    science_marks = 70
    music_marks = 80
    social_marks = 85
    physics_marks = music_marks / 2

    # Calculate the total marks
    total_marks = science_marks + music_marks + social_marks + physics_marks

    # Display the total marks
    result = total_marks
    return result

print(solution())