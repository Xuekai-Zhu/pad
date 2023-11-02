def solution():
    """Martiza is studying for the citizenship test. There are 60 questions on the test. 30 are multiple-choice and 30 are fill-in-the-blank. It takes her 15 minutes to learn each multiple-choice question and 25 minutes each to learn the fill-in-the-blank questions. How many hours will she need to study before she is ready for the test?"""
    mc_questions = 30
    fib_questions = 30
    mc_time = 15
    fib_time = 25
    total_study_time = (mc_questions * mc_time + fib_questions * fib_time) / 60
    result = total_study_time
    return result

print(solution())