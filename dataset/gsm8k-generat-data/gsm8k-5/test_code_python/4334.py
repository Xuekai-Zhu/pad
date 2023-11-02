def solution():
    english_time = 60  # Joan has 1 hour to answer the English exam
    math_time = 90  # Joan has 1.5 hours to answer the Math exam
    english_questions = 30  # The English exam has 30 questions
    math_questions = 15  # The Math exam has 15 questions

    # Calculate the amount of time Joan has for each English question
    english_time_per_question = english_time / english_questions

    # Calculate the amount of time Joan should have for each Math question
    math_time_per_question = math_time / math_questions

    # Calculate the difference in time per question between the Math and English exams
    time_difference = (math_time_per_question - english_time_per_question) * 60

    result = time_difference
    return result

print(solution())