def solution():
    """Sally received the following scores on her math quizzes: 50, 80, 80, 60, 40, 90, 100, 70, and 60. Find her mean score."""
    scores = [50, 80, 80, 60, 40, 90, 100, 70, 60]
    total_score = sum(scores)
    num_scores = len(scores)
    mean_score = total_score / num_scores
    result = mean_score
    return result

print(solution())