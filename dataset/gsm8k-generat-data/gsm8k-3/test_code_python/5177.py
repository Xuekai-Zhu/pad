def solution():
    """Sylvia had one-fifth of incorrect answers in the exam, while Sergio got 4 mistakes. If there were 50 questions, how many more correct answers does Sergio have than Sylvia?"""
    # Define the total number of questions on the exam
    TOTAL_QUESTIONS = 50

    # Calculate Sylvia's number of incorrect answers
    sylvia_incorrect = TOTAL_QUESTIONS / 5

    # Calculate Sylvia's number of correct answers
    sylvia_correct = TOTAL_QUESTIONS - sylvia_incorrect

    # Calculate Sergio's number of correct answers
    sergio_correct = TOTAL_QUESTIONS - 4

    # Calculate the difference in correct answers between Sylvia and Sergio
    difference = sergio_correct - sylvia_correct

    # Display the difference in correct answers
    result = difference
    return result

print(solution())