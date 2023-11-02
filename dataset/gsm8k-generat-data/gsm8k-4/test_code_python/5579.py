def solution():
    """Amaya scored 20 marks fewer in Maths than she scored in Arts. She also got 10 marks more in Social Studies than she got in Music. If she scored 70 in Music and scored 1/10 less in Maths, what's the total number of marks she scored in all the subjects?"""
    # Define the score in music
    music_score = 70

    # Calculate the score in math as 1/10 less than the score in arts
    math_score = 0.9 * (music_score + 20)

    # Calculate the score in social studies as 10 more than the score in music
    social_score = music_score + 10

    # Calculate the total score in all subjects
    total_score = music_score + math_score + social_score

    result = total_score
    return result

print(solution())