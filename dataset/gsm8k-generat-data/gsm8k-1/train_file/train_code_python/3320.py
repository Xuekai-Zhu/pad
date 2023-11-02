def solution():
    """John took a test with 80 questions. For the first 40 questions, she got 90% right. For the next 40 questions, she gets 95% right. How many total questions does she get right?"""
    first_40_percent = 90
    second_40_percent = 95
    total_questions = 80
    first_40_correct = int(first_40_percent / 100 * 40)
    second_40_correct = int(second_40_percent / 100 * 40)
    total_correct = first_40_correct + second_40_correct
    result = total_correct
    return result

print(solution())