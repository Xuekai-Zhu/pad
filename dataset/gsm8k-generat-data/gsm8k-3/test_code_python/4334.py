def solution():
    """Joan is answering English and Math exams with 30 and 15 questions, respectively. The English exam is to be completed in 1 hour and the Math exam in 1.5 hours. If Joan wants to spend an equal amount of time on each question, how many more minutes does she have in answering each question on the Math exam than the English exam?"""
    # Define the number of questions and total time for each exam
    ENGLISH_QUESTIONS = 30
    ENGLISH_TIME = 60 # minutes
    MATH_QUESTIONS = 15
    MATH_TIME = 90 # minutes

    # Calculate the time per question for each exam
    english_time_per_question = ENGLISH_TIME / ENGLISH_QUESTIONS
    math_time_per_question = MATH_TIME / MATH_QUESTIONS

    # Calculate the difference in time per question
    time_diff = math_time_per_question - english_time_per_question

    # Convert the time difference to minutes
    time_diff_minutes = time_diff * 60

    # Display the time difference in minutes
    result = time_diff_minutes
    return result

print(solution())