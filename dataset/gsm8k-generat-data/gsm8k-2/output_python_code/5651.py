def solution():
    """A mathematician is working on two projects. He has one week to write 518 maths questions for one project and 476 questions for another project. If he completes the same number of questions every day, how many should he aim to complete each day?"""
    total_questions = 518 + 476
    days_to_complete = 7
    questions_per_day = total_questions / days_to_complete
    result = questions_per_day
    return result

print(solution())