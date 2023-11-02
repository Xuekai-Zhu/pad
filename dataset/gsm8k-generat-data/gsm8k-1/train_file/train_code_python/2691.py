def solution():
    """Randy got 90, 98, 92, and 94 in his first four quizzes. His goal is to get a 94 average on his 5 quizzes. What score should he get in the fifth quiz to reach his desired average?"""
    goal_average = 94
    first_four_average = (90 + 98 + 92 + 94) / 4
    fifth_score_needed = (goal_average * 5) - (90 + 98 + 92 + 94)
    result = fifth_score_needed
    return result

print(solution())