def solution():
    """After evaluating his students on the final exams. Professor Oscar reviews all 10 questions on each exam. How many questions must he review if he has 5 classes with 35 students each?"""
    num_classes = 5
    num_students_per_class = 35
    num_questions_per_exam = 10
    total_questions = num_classes * num_students_per_class * num_questions_per_exam
    result = total_questions
    return result

print(solution())