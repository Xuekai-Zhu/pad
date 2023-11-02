def solution():
    """After evaluating his students on the final exams. Professor Oscar reviews all 10 questions on each exam. How many questions must he review if he has 5 classes with 35 students each?"""
    # Define the number of classes and students per class
    num_classes = 5
    students_per_class = 35

    # Calculate the total number of students
    total_students = num_classes * students_per_class

    # Calculate the total number of questions to be reviewed
    total_questions = total_students * 10

    # return the result
    result = total_questions
    return result

print(solution())