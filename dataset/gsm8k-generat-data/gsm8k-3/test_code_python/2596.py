def solution():
    """Henry scored 50 points on his Geography test, 70 on his Math test and 66 on his English test. If his History score is the average of these 3 scores, what was his total score across all 4 subjects?"""
    # Define Henry's scores in Geography, Math and English
    geo_score = 50
    math_score = 70
    eng_score = 66

    # Calculate Henry's average score in History
    hist_score = (geo_score + math_score + eng_score) / 3

    # Calculate Henry's total score across all 4 subjects
    total_score = geo_score + math_score + eng_score + hist_score

    # Display Henry's total score
    result = total_score
    return result

print(solution())