def solution():
    
    essay_time = 60
    paragraph_time = 15
    short_answer_time = 3
    total_time = 4 * 60  
    total_assignment_time = (2 * essay_time) + (5 * paragraph_time)
    remaining_time = total_time - total_assignment_time
    num_short_answers = remaining_time // short_answer_time
    result = num_short_answers
    return result

print(solution())