def solution():
    """In a spelling contest held in her school, Drew got 20 questions correct, winning her the competition. She got six questions wrong, and her competitor Carla got 14 questions correct, and twice as many questions wrong as the number of questions Drew got wrong. If each competitor was asked a different question, how many questions were asked in the competition?"""
    # Define the number of correct and wrong answers for Drew
    drew_correct = 20
    drew_wrong = 6

    # Define the number of correct and wrong answers for Carla
    carla_correct = 14
    carla_wrong = drew_wrong * 2

    # Calculate the total number of questions asked
    total_questions = drew_correct + drew_wrong + carla_correct + carla_wrong

    # return the result
    result = total_questions
    return result

print(solution())