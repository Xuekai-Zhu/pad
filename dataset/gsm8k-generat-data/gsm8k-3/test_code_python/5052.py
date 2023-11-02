def solution():
    """After evaluating his students on the final exams. Professor Oscar reviews all 10 questions on each exam. How many questions must he review if he has 5 classes with 35 students each?"""
    # Define the number of questions per exam and the number of students per class
    QUESTIONS_PER_EXAM = 10
    STUDENTS_PER_CLASS = 35

    # Calculate the total number of students
    total_students = 5 * STUDENTS_PER_CLASS

    # Calculate the total number of questions to review
    total_questions = total_students * QUESTIONS_PER_EXAM

    # Display the total number of questions to review
    result = total_questions
    return result

print(solution())