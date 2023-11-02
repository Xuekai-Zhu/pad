def solution():
    """A mathematician is working on two projects. He has one week to write 518 maths questions for one project and 476 questions for another project. If he completes the same number of questions every day, how many should he aim to complete each day?"""
    days_in_week = 7
    total_questions = 518 + 476
    questions_per_day = total_questions / days_in_week
    result = questions_per_day
    return result

print(solution())