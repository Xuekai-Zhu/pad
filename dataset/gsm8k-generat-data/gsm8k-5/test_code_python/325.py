def solution():
    # Bob created 13 questions in the first hour
    hour_one = 13
    
    # Bob doubled his rate for the second hour
    hour_two = hour_one * 2
    
    # Bob doubled his second hour rate for the third hour
    hour_three = hour_two * 2
    
    # Calculate the total number of questions created in three hours
    total_questions = hour_one + hour_two + hour_three
    result = total_questions
    return result

print(solution())