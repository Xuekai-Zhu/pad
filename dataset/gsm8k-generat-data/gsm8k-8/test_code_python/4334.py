def solution():
    # Define the number of questions and time for each exam
    english_questions = 30
    math_questions = 15
    english_time = 60
    math_time = 90

    # Calculate the time per question for each exam
    english_time_per_question = english_time / english_questions
    math_time_per_question = math_time / math_questions

    # Calculate the difference in time per question
    time_diff = math_time_per_question - english_time_per_question

    # Convert the time difference to minutes and round to the nearest integer
    time_diff_minutes = round(time_diff * 60)

    result = time_diff_minutes
    return result

print(solution())