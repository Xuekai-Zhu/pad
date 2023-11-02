def solution():
    """Amaya scored 20 marks fewer in Maths than she scored in Arts. She also got 10 marks more in Social Studies than she got in Music. If she scored 70 in Music and scored 1/10 less in Maths, what's the total number of marks she scored in all the subjects?"""
    # Define the score in Music
    music_score = 70

    # Calculate the score in Maths
    math_score = music_score * 0.9 - 20

    # Calculate the score in Arts
    arts_score = math_score + 20

    # Calculate the score in Social Studies
    social_score = music_score + 10

    # Calculate the total score
    total_score = music_score + math_score + arts_score + social_score

    # Display the total score
    result = total_score
    return result

print(solution())