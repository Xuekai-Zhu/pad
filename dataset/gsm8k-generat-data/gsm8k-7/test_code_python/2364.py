def solution():
    num_students = 25
    target_avg_score = 75
    current_avg_score = 77
    sum_of_scores = current_avg_score * (num_students - 1)

    # Calculate the minimum score the absent student can get to maintain the target average score
    min_absent_score = (target_avg_score * num_students) - sum_of_scores
    result = min_absent_score

    return result

print(solution())