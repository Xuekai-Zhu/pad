def solution():
    drew_correct = 20
    drew_wrong = 6
    carla_correct = 14
    carla_wrong = drew_wrong * 2

    # Calculate the total number of questions
    total_questions = drew_correct + drew_wrong + carla_correct + carla_wrong
    result = total_questions
    return result

print(solution())