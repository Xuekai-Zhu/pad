def solution():
    num_mc_questions = 30
    num_fib_questions = 30
    mc_question_time = 15
    fib_question_time = 25

    # Calculate the total time Martiza will spend studying the multiple-choice questions
    total_mc_time = num_mc_questions * mc_question_time

    # Calculate the total time Martiza will spend studying the fill-in-the-blank questions
    total_fib_time = num_fib_questions * fib_question_time

    # Calculate the total time Martiza will spend studying for the test in hours
    total_time = (total_mc_time + total_fib_time) / 60.0
    result = total_time
    return result

print(solution())