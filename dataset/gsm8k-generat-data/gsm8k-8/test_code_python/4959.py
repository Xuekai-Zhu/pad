def solution():
    # Define the total number of questions needed to write
    total_questions = 50

    # Define the number of multiple-choice questions already written
    mc_questions_written = 14

    # Define the number of problem-solving questions already written
    ps_questions_written = 5

    # Calculate the total number of questions still needed to write
    questions_left = total_questions - mc_questions_written - ps_questions_written
    result = questions_left
    return result

print(solution())