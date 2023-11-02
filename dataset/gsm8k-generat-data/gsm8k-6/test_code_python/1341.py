def solution():
    # Calculate the total number of questions Sasha can complete in 2 hours
    total_questions = 15 * 2

    # Calculate how many questions Sasha still needs to complete
    questions_remaining = 60 - total_questions
    result = questions_remaining
    return result

print(solution())