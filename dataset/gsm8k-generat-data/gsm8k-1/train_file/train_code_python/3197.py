def solution():
    """In a spelling contest held in her school, Drew got 20 questions correct, winning her the competition. She got six questions wrong, and her competitor Carla got 14 questions correct, and twice as many questions wrong as the number of questions Drew got wrong. If each competitor was asked a different question, how many questions were asked in the competition?"""
    questions_correct_by_drew = 20
    questions_wrong_by_drew = 6
    questions_correct_by_carla = 14
    questions_wrong_by_carla = questions_wrong_by_drew * 2
    
    total_questions_asked = questions_correct_by_drew + questions_wrong_by_drew + questions_correct_by_carla + questions_wrong_by_carla
    result = total_questions_asked
    
    return result

print(solution())