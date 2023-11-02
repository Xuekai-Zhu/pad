def solution():
    
    drew_correct = 20
    drew_wrong = 6
    carla_correct = 14
    carla_wrong = 2 * drew_wrong
    total_correct = drew_correct + carla_correct
    total_wrong = drew_wrong + carla_wrong
    total_questions = total_correct + total_wrong
    result = total_questions
    return result

print(solution())