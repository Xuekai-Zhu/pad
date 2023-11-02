def solution():
    time_for_short_answer = 3
    time_for_paragraph = 15
    time_for_essay = 60
    essays_assigned = 2
    paragraphs_assigned = 5
    total_time_assigned = 4
    total_time_used = (essays_assigned * time_for_essay) + (paragraphs_assigned * time_for_paragraph)
    time_left = total_time_assigned - total_time_used
    short_answer_questions = time_left / time_for_short_answer
    result = short_answer_questions
    
    return result

print(solution())