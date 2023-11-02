def solution():
    total_questions = 518 + 476  # The mathematician has to write a total of 518+476 questions
    days = 7  # The mathematician has one week to complete the questions

    # Calculate how many questions the mathematician needs to complete per day
    questions_per_day = total_questions / days
    result = questions_per_day
    return result

print(solution())