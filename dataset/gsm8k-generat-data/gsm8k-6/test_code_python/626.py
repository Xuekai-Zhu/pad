def solution():
    # Calculate Jessica's current pace
    pace = 12 / 16  # minutes per question
    
    # Calculate the remaining time based on the same pace
    remaining_questions = 80 - 16
    remaining_time = (remaining_questions * pace) + 12
    
    # Convert remaining time to minutes
    remaining_minutes = remaining_time % 60
    
    result = remaining_minutes
    return result

print(solution())