def solution():
    """The result from the 40-item Statistics exam Marion and Ella took already came out. Ella got 4 incorrect answers while Marion got 6 more than half the score of Ella. What is Marion's score?"""
    # Define the total number of items in the exam
    total_items = 40

    # Calculate the number of correct answers of Ella
    ella_correct = total_items - 4

    # Calculate the score of Ella
    ella_score = ella_correct / total_items

    # Calculate the score of Marion
    marion_score = ella_score * 0.5 + 0.3

    # Convert the score to a percentage
    marion_percentage = marion_score * 100

    # return the result
    result = marion_percentage
    return result

print(solution())