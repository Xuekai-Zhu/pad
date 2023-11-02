def solution():
    
    questions_correct_by_drew = 20
    questions_wrong_by_drew = 6
    questions_correct_by_carla = 14
    questions_wrong_by_carla = questions_wrong_by_drew * 2
    
    total_questions_asked = questions_correct_by_drew + questions_wrong_by_drew + questions_correct_by_carla + questions_wrong_by_carla
    result = total_questions_asked
    
    return result

print(solution())