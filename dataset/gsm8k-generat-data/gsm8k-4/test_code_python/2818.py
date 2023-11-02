def solution():
    """Teresa scored 70 marks in science, 80 in music, 85 in social studies, and the physics exam, which was the hardest test that Teresa had ever taken in her entire life, she scored half as many marks as she scored in music. Calculate the total marks Teresa scored in all the subjects."""
    # Define the scores in each subject
    science_score = 70
    music_score = 80
    social_studies_score = 85
    physics_score = music_score / 2

    # Calculate the total marks
    total_score = science_score + music_score + social_studies_score + physics_score

    # Return the result
    result = total_score
    return result

print(solution())