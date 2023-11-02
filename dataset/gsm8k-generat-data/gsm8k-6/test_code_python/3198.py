def solution():
    # Calculate the total number of questions in the spelling contest
    drew_wrong = 6
    carla_wrong = 2 * drew_wrong
    drew_total = drew_wrong + 20
    carla_total = carla_wrong + 14
    total_questions = drew_total + carla_total
    result = total_questions
    return result

print(solution())