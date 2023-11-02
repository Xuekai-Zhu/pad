def solution():
    """Bob was creating a math test for an online platform. He created 13 questions in the first hour. Bob then doubled his rate for the second hour, and doubled his second hour rate for the third hour. How many questions did Bob create in the three hours?"""
    first_hour = 13
    second_hour = first_hour * 2
    third_hour = second_hour * 2
    total_questions = first_hour + second_hour + third_hour
    result = total_questions
    return result

print(solution())