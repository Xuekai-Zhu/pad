def solution():
    total_questions = 80  # John took a test with 80 questions
    first_40_questions_percent = 90  # John got 90% of the first 40 questions right
    next_40_questions_percent = 95  # John got 95% of the next 40 questions right

    # Calculate the number of questions John got right in the first 40
    first_40_questions_right = int((first_40_questions_percent / 100) * 40)

    # Calculate the number of questions John got right in the next 40
    next_40_questions_right = int((next_40_questions_percent / 100) * 40)

    # Calculate the total number of questions John got right
    total_questions_right = first_40_questions_right + next_40_questions_right
    result = total_questions_right
    return result

print(solution())