def solution():
    """Joan is answering English and Math exams with 30 and 15 questions, respectively. 
    The English exam is to be completed in 1 hour and the Math exam in 1.5 hours. 
    If Joan wants to spend an equal amount of time on each question, how many more 
    minutes does she have in answering each question on the Math exam than the English exam?"""
    # Define the number of questions and time allowed for each exam
    english_questions = 30
    math_questions = 15
    english_time = 60   # in minutes
    math_time = 90      # in minutes

    # Calculate the time allowed for each English question
    english_time_per_question = english_time / english_questions

    # Calculate the time allowed for each Math question
    math_time_per_question = math_time / math_questions

    # Calculate the difference in time allowed per question
    time_difference = math_time_per_question - english_time_per_question

    # Convert the time difference to minutes
    time_difference_minutes = time_difference * 60

    # Return the time difference in minutes
    result = time_difference_minutes
    return result

print(solution())