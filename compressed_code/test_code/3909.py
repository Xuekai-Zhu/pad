def solution():
    
    num_classes = 5
    num_students_per_class = 35
    num_questions_per_exam = 10
    total_num_students = num_classes * num_students_per_class
    total_num_questions = total_num_students * num_questions_per_exam
    result = total_num_questions
    return result

print(solution())