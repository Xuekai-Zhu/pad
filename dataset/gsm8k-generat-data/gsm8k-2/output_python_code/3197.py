def solution():
    """In a spelling contest held in her school, Drew got 20 questions correct, winning her the competition. She got six questions wrong, and her competitor Carla got 14 questions correct, and twice as many questions wrong as the number of questions Drew got wrong. If each competitor was asked a different question, how many questions were asked in the competition?"""
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