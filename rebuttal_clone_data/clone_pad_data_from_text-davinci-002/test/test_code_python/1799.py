def solution():
    
    correct_drew = 20
    wrong_drew = 6
    correct_carla = 14
    wrong_carla = 2 * wrong_drew
    total_correct = correct_drew + correct_carla
    total_wrong = wrong_drew + wrong_carla
    total_questions = total_correct + total_wrong
    result = total_questions
    return result

print(solution())