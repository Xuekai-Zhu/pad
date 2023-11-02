def solution():
    
    total_students = 25
    target_average = 75
    current_average = 77
    sum_of_scores = current_average * (total_students - 1)
    minimum_score_needed = (target_average * total_students) - sum_of_scores
    result = minimum_score_needed
    return result

print(solution())