def solution():
    num_classes = 5
    num_students_per_class = 35
    num_questions_per_exam = 10

    # Calculate the total number of students
    total_students = num_classes * num_students_per_class

    # Calculate the total number of questions
    total_questions = total_students * num_questions_per_exam
    result = total_questions
    return result

print(solution())