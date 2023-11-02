def solution():
    # Define the given information
    total_questions = 60
    questions_per_hour = 15
    hours_worked = 2

    # Calculate the total number of questions Sasha can complete in 2 hours
    completed_questions = questions_per_hour * hours_worked
    
    # Calculate the number of questions Sasha still needs to complete
    remaining_questions = total_questions - completed_questions
    
    result = remaining_questions
    return result

print(solution())