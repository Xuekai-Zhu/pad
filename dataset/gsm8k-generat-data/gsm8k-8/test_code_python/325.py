def solution():
    # Define the number of questions Bob created in each hour
    first_hour = 13
    second_hour = 2 * first_hour
    third_hour = 2 * second_hour

    # Calculate the total number of questions created
    total_questions = first_hour + second_hour + third_hour
    result = total_questions
    return result

print(solution())