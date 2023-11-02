def solution():
    """Jessica has one hour to take an exam. She has answered 16 out of 80 questions. She has used 12 minutes of her time. If she keeps up this same pace, how many minutes will be left when she finishes the exam?"""
    total_questions = 80
    remaining_questions = total_questions - 16
    remaining_time = (remaining_questions / 64) * 48
    total_time = 60
    time_left = total_time - remaining_time - 12
    result = time_left
    return result

print(solution())