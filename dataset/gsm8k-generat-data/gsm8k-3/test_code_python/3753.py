def solution():
    """Out of 804 senior high school students, 75% passed their exams and so got their degree. The rest failed. How many didn't pass their exams?"""
    # Define the total number of senior high school students
    total_students = 804

    # Calculate the number of students who passed their exams
    passed_students = int(total_students * 0.75)

    # Calculate the number of students who didn't pass their exams
    failed_students = total_students - passed_students

    # Display the number of students who didn't pass their exams
    result = failed_students
    return result

print(solution())