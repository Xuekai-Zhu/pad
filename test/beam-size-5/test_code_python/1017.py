def solution():
    
    total_items = 60
    easy_questions = total_items * 0.4
    difficult_questions = total_items - easy_questions
    easy_points = easy_questions * 0.75
    average_points = average_questions * 0.5
    difficult_points = difficult_questions * 0.5
    total_points = easy_points + average_points + difficult_points
    result = total_points
    return result

print(solution())