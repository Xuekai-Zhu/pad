def solution():
    # Calculate the total score Randy needs to get with 5 quizzes
    total_needed = 94 * 5  

    # Calculate Randy's current total score
    current_total = sum([90, 98, 92, 94])  

    # Calculate the score Randy needs to get on the fifth quiz to average 94
    score_needed = total_needed - current_total  

    result = score_needed
    return result

print(solution())