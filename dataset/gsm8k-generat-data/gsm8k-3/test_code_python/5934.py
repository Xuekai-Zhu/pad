def solution():
    """Ms. Cole teaches math in three levels of classes in her school. There are four times as many students in Ms. Cole's fourth-level math class as in her sixth-level math class. The number of students in her seventh-level math class is twice that in the fourth-level math class.  If Ms. Cole's sixth-level class has 40 students, how many math students does Ms. Cole teach?"""
    # Determine the number of students in the sixth-level math class
    students_6 = 40

    # Determine the number of students in the fourth-level math class
    students_4 = students_6 * 4

    # Determine the number of students in the seventh-level math class
    students_7 = students_4 * 2

    # Calculate the total number of math students Ms. Cole teaches
    total_students = students_6 + students_4 + students_7

    # Display the total number of math students
    result = total_students
    return result

print(solution())