def solution():
    """Bob was creating a math test for an online platform.  He created 13 questions in the first hour.  Bob then doubled his rate for the second hour, and doubled his second hour rate for the third hour.  How many questions did Bob create in the three hours?"""
    # Bob's rate per hour for the first hour
    rate1 = 13

    # Bob's rate per hour for the second hour
    rate2 = rate1 * 2

    # Bob's rate per hour for the third hour
    rate3 = rate2 * 2

    # Calculate the total number of questions Bob created
    total_questions = rate1 + rate2 + rate3

    # Display the total number of questions
    result = total_questions
    return result

print(solution())