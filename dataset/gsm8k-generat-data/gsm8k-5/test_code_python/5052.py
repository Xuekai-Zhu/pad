def solution():
    questions_per_exam = 10  # Professor Oscar reviews 10 questions on each exam
    students_per_class = 35  # Each class has 35 students
    num_of_classes = 5  # Professor Oscar has 5 classes to review

    # Calculate the total number of questions Professor Oscar must review
    total_questions = questions_per_exam * students_per_class * num_of_classes
    result = total_questions
    return result

print(solution())