def solution():
    
    music_score = 70
    math_score = music_score * 0.9
    arts_score = math_score + 20
    social_studies_score = music_score + 10
    total_score = music_score + math_score + arts_score + social_studies_score
    result = total_score
    return result

print(solution())