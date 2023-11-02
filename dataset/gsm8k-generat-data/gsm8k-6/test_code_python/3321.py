def solution():
    # Calculate the number of questions she got right in the first 40 questions
    first_40 = 0.9 * 40  

    # Calculate the number of questions she got right in the next 40 questions
    next_40 = 0.95 * 40  

    # Calculate the total number of questions she got right
    total_questions_right = first_40 + next_40  
    result = total_questions_right
    return result

print(solution())