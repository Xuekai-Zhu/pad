def solution():
    """Amy is taking a history test. She correctly answers 80% of the multiple-choice questions, 90% of the true/false questions, and 60% of the long-answer questions. The multiple-choice and true/false questions are worth 1 point each, and the long answer questions are worth 5 points each. How many points does Amy score if there are 10 multiple-choice questions, 20 true/false questions, and 5 long answer questions?"""
    mcq_correct = 0.8 * 10
    tf_correct = 0.9 * 20
    la_correct = 0.6 * 5
    mcq_points = mcq_correct
    tf_points = tf_correct
    la_points = la_correct * 5
    total_points = mcq_points + tf_points + la_points
    result = total_points
    return result

print(solution())