def solution():
    # Define the number of classes and students
    num_classes = 5
    num_students_per_class = 35

    # Define the number of questions per exam
    num_questions_per_exam = 10

    # Calculate the total number of questions to review
    total_questions_to_review = num_classes * num_students_per_class * num_questions_per_exam

    result = total_questions_to_review
    return result

print(solution())