def solution():
    """Martiza is studying for the citizenship test. There are 60 questions on the test. 30 are multiple-choice and 30 are fill-in-the-blank. It takes her 15 minutes to learn each multiple-choice question and 25 minutes each to learn the fill-in-the-blank questions. How many hours will she need to study before she is ready for the test?"""
    # Define the number of multiple-choice questions and the time it takes to learn each one
    multiple_choice_questions = 30
    multiple_choice_time = 15

    # Define the number of fill-in-the-blank questions and the time it takes to learn each one
    fill_in_the_blank_questions = 30
    fill_in_the_blank_time = 25

    # Calculate the total time needed to learn all the multiple-choice questions
    total_multiple_choice_time = multiple_choice_questions * multiple_choice_time

    # Calculate the total time needed to learn all the fill-in-the-blank questions
    total_fill_in_the_blank_time = fill_in_the_blank_questions * fill_in_the_blank_time

    # Calculate the total time needed to study for the test
    total_study_time = (total_multiple_choice_time + total_fill_in_the_blank_time) / 60

    # Return the result in hours
    result = total_study_time
    return result

print(solution())