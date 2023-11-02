def solution():
    """Henry scored 50 points on his Geography test, 70 on his Math test and 66 on his English test. If his History score is the average of these 3 scores, what was his total score across all 4 subjects?"""
    geography_score = 50
    math_score = 70
    english_score = 66
    history_score = (geography_score + math_score + english_score) / 3
    total_score = geography_score + math_score + english_score + history_score
    result = total_score
    return result

print(solution())