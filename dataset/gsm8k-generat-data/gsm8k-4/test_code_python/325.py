def solution():
    """Bob was creating a math test for an online platform. He created 13 questions in the first hour. Bob then doubled his rate for the second hour, and doubled his second hour rate for the third hour. How many questions did Bob create in the three hours?"""
    # Define the number of questions Bob created in the first hour
    first_hour_questions = 13

    # Calculate the number of questions Bob created in the second hour
    second_hour_questions = first_hour_questions * 2

    # Calculate the number of questions Bob created in the third hour
    third_hour_questions = second_hour_questions * 2

    # Calculate the total number of questions Bob created in three hours
    total_questions = first_hour_questions + second_hour_questions + third_hour_questions

    # return the result
    result = total_questions
    return result

print(solution())