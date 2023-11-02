def solution():
    """Joan is answering English and Math exams with 30 and 15 questions, respectively. The English exam is to be completed in 1 hour and the Math exam in 1.5 hours. If Joan wants to spend an equal amount of time on each question, how many more minutes does she have in answering each question on the Math exam than the English exam?"""
    english_questions = 30
    math_questions = 15
    english_time = 60
    math_time = 90
    english_time_per_question = english_time / english_questions
    math_time_per_question = math_time / math_questions
    extra_time_per_question = math_time_per_question - english_time_per_question
    extra_time_in_minutes = extra_time_per_question * 60
    result = extra_time_in_minutes
    return result

print(solution())