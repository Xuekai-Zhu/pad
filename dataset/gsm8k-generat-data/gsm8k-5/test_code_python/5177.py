def solution():
    num_questions = 50  # There were 50 questions in the exam
    sylvia_incorrect = num_questions / 5  # Sylvia had one-fifth of incorrect answers, so she got 10 questions wrong
    sergio_incorrect = 4  # Sergio had 4 mistakes
    sylvia_correct = num_questions - sylvia_incorrect  # Calculate Sylvia's number of correct answers
    sergio_correct = num_questions - sergio_incorrect  # Calculate Sergio's number of correct answers

    # Calculate the difference in correct answers between Sylvia and Sergio
    correct_difference = sergio_correct - sylvia_correct
    result = correct_difference
    return result

print(solution())