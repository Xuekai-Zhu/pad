def solution():
    """Sasha can complete 15 questions an hour. If she has 60 questions to complete and she works for 2 hours, how many questions does she still need to complete?"""
    # Define the number of questions Sasha can complete in an hour and the total number of questions she has to complete
    questions_per_hour = 15
    total_questions = 60

    # Calculate the total number of hours Sasha needs to complete all the questions
    total_hours = total_questions / questions_per_hour

    # Calculate the number of questions Sasha can complete in 2 hours
    questions_completed = questions_per_hour * 2

    # Calculate the number of questions Sasha still needs to complete after 2 hours
    questions_remaining = total_questions - questions_completed

    # return the result
    result = questions_remaining
    return result

print(solution())