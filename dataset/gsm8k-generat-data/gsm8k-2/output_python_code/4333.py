def solution():
    """Joan is answering English and Math exams with 30 and 15 questions, respectively. The English exam is to be completed in 1 hour and the Math exam in 1.5 hours. If Joan wants to spend an equal amount of time on each question, how many more minutes does she have in answering each question on the Math exam than the English exam?"""
    english_questions = 30
    math_questions = 15
    english_time = 60 / english_questions
    math_time = 90 / math_questions
    time_difference = math_time - english_time
    extra_minutes = time_difference * 60
    result = extra_minutes
    return result

print(solution())