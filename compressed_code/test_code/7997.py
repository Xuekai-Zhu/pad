def solution():
    
    scores = [80, 70, 90]
    avg_score_needed = 85
    total_score_needed = avg_score_needed * 4
    current_total_score = sum(scores)
    score_needed_on_4th_test = total_score_needed - current_total_score
    result = score_needed_on_4th_test
    return result

print(solution())