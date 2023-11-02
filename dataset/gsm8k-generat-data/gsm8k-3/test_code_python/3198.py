def solution():
    """In a spelling contest held in her school, Drew got 20 questions correct, winning her the competition. She got six questions wrong, and her competitor Carla got 14 questions correct, 
    and twice as many questions wrong as the number of questions Drew got wrong. If each competitor was asked a different question, how many questions were asked in the competition?"""
    
    # Calculate the number of questions Drew was asked in total
    drew_total_questions = 20 + 6
    # Calculate the number of questions Carla got wrong
    carla_wrong_questions = 6 * 2
    
    # Calculate the number of questions Carla was asked in total
    carla_total_questions = carla_wrong_questions + 14
    
    # Calculate the total number of questions
    total_questions = drew_total_questions + carla_total_questions
    
    # Display the total number of questions
    result = total_questions
    return result

print(solution())