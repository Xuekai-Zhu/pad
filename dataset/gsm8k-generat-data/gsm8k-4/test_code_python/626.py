def solution():
    """Jessica has one hour to take an exam. She has answered 16 out of 80 questions. She has used 12 minutes of her time. If she keeps up this same pace, how many minutes will be left when she finishes the exam?"""
    # Define the total time available for the exam in minutes
    TOTAL_TIME = 60

    # Calculate the percentage of questions answered so far
    percent_answered = 16 / 80

    # Calculate the percentage of time used so far
    percent_time_used = 12 / 60

    # Calculate the remaining percentage of questions to be answered
    remaining_percent = 1 - percent_answered

    # Calculate the remaining percentage of time left
    remaining_time_percent = 1 - percent_time_used

    # Calculate the time left for the remaining questions
    time_left = (remaining_percent / percent_answered) * (12 / 60)

    # Calculate the total time left
    total_time_left = TOTAL_TIME * remaining_time_percent

    # Calculate the time left when she finishes the exam
    time_left_total = total_time_left - time_left

    result = round(time_left_total * 60)
    return result

print(solution())