def solution():
    """John took a test with 80 questions. For the first 40 questions, she got 90% right. For the next 40 questions, she gets 95% right. How many total questions does she get right?"""
    first_40_correct = 0.9 * 40
    next_40_correct = 0.95 * 40
    total_correct = first_40_correct + next_40_correct
    result = total_correct
    return result

print(solution())