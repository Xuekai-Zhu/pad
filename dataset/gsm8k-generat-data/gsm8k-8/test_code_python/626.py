def solution():
    # Determine how many questions she can answer per minute
    questions_per_minute = 16 / 12
    
    # Determine how many minutes she will need to answer the remaining questions
    remaining_questions = 80 - 16
    remaining_time = remaining_questions / questions_per_minute
    
    # Determine how many minutes will be left when she finishes
    total_time = 60
    time_left = total_time - (12 + remaining_time)
    result = time_left
    return result

print(solution())