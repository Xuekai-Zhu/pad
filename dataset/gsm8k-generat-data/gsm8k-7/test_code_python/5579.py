def solution():
    music_score = 70
    math_score = 0.9 * (music_score + 20)  # scored 1/10 less in math than art
    social_studies_score = music_score + 10
    arts_score = music_score + 20

    # Calculate the total number of marks Amaya scored in all subjects
    total_score = music_score + math_score + social_studies_score + arts_score
    result = total_score
    return result

print(solution())