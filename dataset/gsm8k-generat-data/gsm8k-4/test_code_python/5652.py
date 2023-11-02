def solution():
    """A mathematician is working on two projects. He has one week to write 518 maths questions for one project and 476 questions for another project. If he completes the same number of questions every day, how many should he aim to complete each day?"""
    # Define the number of questions and the time frame
    total_questions = 518 + 476
    time_days = 7

    # Calculate the number of questions to complete each day
    questions_per_day = total_questions / (time_days * 2)

    result = round(questions_per_day)
    return result

print(solution())