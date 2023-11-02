def solution():
    num_multiple_choice = 30  # There are 30 multiple choice questions
    num_fill_in_blank = 30  # There are 30 fill-in-the-blank questions
    time_per_multiple_choice = 15  # It takes 15 minutes to learn each multiple-choice question
    time_per_fill_in_blank = 25  # It takes 25 minutes to learn each fill-in-the-blank question

    # Calculate the total time needed to learn all the multiple-choice questions
    time_for_multiple_choice = num_multiple_choice * time_per_multiple_choice

    # Calculate the total time needed to learn all the fill-in-the-blank questions
    time_for_fill_in_blank = num_fill_in_blank * time_per_fill_in_blank

    # Add the two times together to get the total time needed to study
    total_time = (time_for_multiple_choice + time_for_fill_in_blank) / 60  # Convert minutes to hours

    result = total_time
    return result

print(solution())