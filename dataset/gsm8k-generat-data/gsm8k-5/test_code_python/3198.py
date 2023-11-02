def solution():
    drew_correct = 20  # Drew got 20 questions correct
    drew_wrong = 6  # Drew got 6 questions wrong
    carla_correct = 14  # Carla got 14 questions correct
    carla_wrong = drew_wrong * 2  # Carla got twice as many questions wrong as Drew

    # Calculate the total number of questions asked
    total_questions = drew_correct + drew_wrong + carla_correct + carla_wrong
    result = total_questions
    return result

print(solution())