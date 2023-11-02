def solution():
    # Calculate the number of questions Drew got wrong
    drew_wrong = 6

    # Calculate the number of questions Carla got wrong
    carla_wrong = 2 * drew_wrong

    # Calculate the total number of correct answers
    total_correct = 20 + 14

    # Calculate the total number of questions
    total_questions = total_correct + drew_wrong + carla_wrong
    result = total_questions
    return result

print(solution())