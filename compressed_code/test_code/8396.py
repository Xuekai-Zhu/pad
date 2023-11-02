def solution():
    
    time_per_short_answer = 3 / 60  
    time_per_paragraph = 15 / 60  
    time_per_essay = 1
    num_essays = 2
    num_paragraphs = 5
    total_time = 4  
    time_spent_on_essays = num_essays * time_per_essay
    time_spent_on_paragraphs = num_paragraphs * time_per_paragraph
    remaining_time = total_time - time_spent_on_essays - time_spent_on_paragraphs
    num_short_answers = remaining_time / time_per_short_answer
    result = num_short_answers

    return result

print(solution())