def solution():
    """Martiza is studying for the citizenship test. There are 60 questions on the test. 30 are multiple-choice and 30 are fill-in-the-blank. It takes her 15 minutes to learn each multiple-choice question and 25 minutes each to learn the fill-in-the-blank questions. How many hours will she need to study before she is ready for the test?"""
    # Define the number of multiple-choice questions and fill-in-the-blank questions
    num_multiple_choice = 30
    num_fill_in_blank = 30

    # Define the time it takes to learn each type of question
    time_per_multiple_choice = 15
    time_per_fill_in_blank = 25

    # Calculate the total time Martiza needs to study
    total_time = (num_multiple_choice * time_per_multiple_choice + num_fill_in_blank * time_per_fill_in_blank) / 60

    # Display the total time in hours
    result = total_time
    return result

print(solution())