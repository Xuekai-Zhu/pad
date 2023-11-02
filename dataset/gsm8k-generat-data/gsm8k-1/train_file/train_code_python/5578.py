def solution():
    """Amaya scored 20 marks fewer in Maths than she scored in Arts. She also got 10 marks more in Social Studies than she got in Music. If she scored 70 in Music and scored 1/10 less in Maths, what's the total number of marks she scored in all the subjects?"""
    arts_score = 70 + 20
    maths_score = arts_score - 20 - (1/10 * arts_score)
    social_score = 70 + 10
    total_score = arts_score + maths_score + social_score + 70
    result = total_score
    return result

print(solution())