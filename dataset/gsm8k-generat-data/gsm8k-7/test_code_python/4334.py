def solution():
    english_questions = 30
    english_time = 60  # in minutes
    math_questions = 15
    math_time = 90  # in minutes

    # Calculate the time allotted for each English question
    english_question_time = english_time / english_questions

    # Calculate the time allotted for each Math question
    math_question_time = math_time / math_questions

    # Calculate the difference in time allotted for each question
    time_difference = math_question_time - english_question_time

    # Convert the time difference into minutes
    extra_minutes = time_difference * 60
    result = extra_minutes
    return result

print(solution())