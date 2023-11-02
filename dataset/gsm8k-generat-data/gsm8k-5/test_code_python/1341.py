def solution():
    questions_per_hour = 15  # Sasha can complete 15 questions in an hour
    total_questions = 60  # Sasha has 60 questions to complete
    hours_worked = 2  # Sasha will work for 2 hours

    # Calculate the total number of questions Sasha can complete in the given time
    total_completed = questions_per_hour * hours_worked

    # Calculate the number of questions Sasha still needs to complete
    remaining_questions = total_questions - total_completed
    result = remaining_questions
    return result

print(solution())