def solution():
    """The result from the 40-item Statistics exam Marion and Ella took already came out. Ella got 4 incorrect answers while Marion got 6 more than half the score of Ella. What is Marion's score?"""
    total_questions = 40
    ella_incorrect = 4
    ella_correct = total_questions - ella_incorrect
    marion_correct = (ella_correct / 2) + 6
    marion_score = (marion_correct / total_questions) * 100
    result = marion_score
    return result

print(solution())