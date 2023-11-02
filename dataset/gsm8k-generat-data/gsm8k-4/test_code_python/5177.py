def solution():
    """Sylvia had one-fifth of incorrect answers in the exam, while Sergio got 4 mistakes. If there were 50 questions, how many more correct answers does Sergio have than Sylvia?"""
    # Define the total number of questions
    total_questions = 50

    # Calculate the number of questions Sylvia got wrong
    sylvia_wrong = total_questions / 5

    # Calculate the number of questions Sylvia got right
    sylvia_right = total_questions - sylvia_wrong

    # Calculate the number of questions Sergio got right
    sergio_right = total_questions - 4

    # Calculate the difference in the number of correct answers
    difference = sergio_right - sylvia_right

    # return the result
    result = difference
    return result

print(solution())