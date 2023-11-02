def solution():
    """Henry scored 50 points on his Geography test, 70 on his Math test and 66 on his English test. If his History score is the average of these 3 scores, what was his total score across all 4 subjects?"""
    geo_score = 50
    math_score = 70
    eng_score = 66
    hist_score = (geo_score + math_score + eng_score) / 3
    total_score = geo_score + math_score + eng_score + hist_score
    result = total_score
    return result

print(solution())