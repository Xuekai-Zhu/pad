def solution():
    
    geo_score = 50
    math_score = 70
    eng_score = 66
    hist_score = (geo_score + math_score + eng_score) / 3
    total_score = geo_score + math_score + eng_score + hist_score
    result = total_score
    return result

print(solution())