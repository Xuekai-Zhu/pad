def solution():
    average_needed = 93
    quizzes_taken = 4
    current_average = 92
    score_needed = (average_needed * (quizzes_taken + 1)) - (current_average * quizzes_taken)
    result = score_needed
    return result

print(solution())