def solution():
    """The result from the 40-item Statistics exam Marion and Ella took already came out. Ella got 4 incorrect answers while Marion got 6 more than half the score of Ella. What is Marion's score?"""
    total_items = 40
    ella_wrong = 4
    ella_correct = total_items - ella_wrong
    marion_correct = (ella_correct / 2) + 6
    marion_score = (marion_correct / total_items) * 100
    result = marion_score
    return result

print(solution())