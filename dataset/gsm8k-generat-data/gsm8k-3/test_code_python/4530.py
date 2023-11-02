def solution():
    """The result from the 40-item Statistics exam Marion and Ella took already came out. Ella got 4 incorrect answers while Marion got 6 more than half the score of Ella. What is Marion's score?"""
    # Define the total number of items in the exam
    total_items = 40

    # Calculate the number of correct answers for Ella
    ella_correct = total_items - 4

    # Calculate half of Ella's score
    ella_half = ella_correct / 2

    # Calculate Marion's score
    marion_score = ella_half + 6

    # Display Marion's score
    result = marion_score
    return result

print(solution())