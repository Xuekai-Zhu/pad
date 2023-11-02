def solution():
    """Bob was creating a math test for an online platform. He created 13 questions in the first hour. Bob then doubled his rate for the second hour, and doubled his second hour rate for the third hour. How many questions did Bob create in the three hours?"""
    q1 = 13
    q2 = q1 * 2
    q3 = q2 * 2
    total_questions = q1 + q2 + q3
    result = total_questions
    return result

print(solution())