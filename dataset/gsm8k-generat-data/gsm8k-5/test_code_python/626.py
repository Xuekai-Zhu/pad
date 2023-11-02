def solution():
    total_questions = 80  # Total number of questions in the exam
    answered_questions = 16  # Number of questions Jessica has already answered
    remaining_questions = total_questions - answered_questions  # Number of questions Jessica still needs to answer
    remaining_time = 60 - 12  # Jessica has used 12 minutes of her 1 hour exam time

    # Calculate the average time Jessica takes to answer each remaining question
    time_per_question = remaining_time / (remaining_questions * 1.0)

    # Calculate the total time Jessica will take to finish the exam
    total_time = remaining_time + (time_per_question * remaining_questions)

    # Calculate the time left when Jessica finishes the exam
    time_left = 60 - total_time
    result = time_left
    return result

print(solution())