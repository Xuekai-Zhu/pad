def solution():
    """Randy got 90, 98, 92, and 94 in his first four quizzes. His goal is to get a 94 average on his 5 quizzes. What score should he get in the fifth quiz to reach his desired average?"""
    current_total = 90 + 98 + 92 + 94
    desired_total = 94 * 5
    fifth_quiz_score = desired_total - current_total
    result = fifth_quiz_score
    return result

print(solution())