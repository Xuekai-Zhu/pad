def solution():
    """Jessica has one hour to take an exam. She has answered 16 out of 80 questions. She has used 12 minutes of her time. If she keeps up this same pace, how many minutes will be left when she finishes the exam?"""
    questions_answered = 16
    total_questions = 80
    time_used = 12
    time_per_question = time_used / questions_answered
    time_remaining = (total_questions - questions_answered) * time_per_question
    time_left = 60 - time_used - time_remaining
    result = time_left
    return result

print(solution())