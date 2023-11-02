def solution():
    # Calculate the total time spent on essays and paragraphs
    total_time = 2*60 + 5*15  # 2 essays take 2 hours and 5 paragraphs take 75 minutes 

    # Calculate the remaining time for short answer questions
    remaining_time = 4*60 - total_time

    # Calculate the number of short answer questions Karen should assign
    saq_count = remaining_time // 3 

    result = saq_count
    return result

print(solution())