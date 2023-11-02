def solution():
    """Ms. Cole teaches math in three levels of classes in her school. There are four times as many students in Ms. Cole's fourth-level math class as in her sixth-level math class. The number of students in her seventh-level math class is twice that in the fourth-level math class. If Ms. Cole's sixth-level class has 40 students, how many math students does Ms. Cole teach?"""
    # Define the number of students in the sixth-level math class
    sixth_level_students = 40

    # Calculate the number of students in the fourth-level math class
    fourth_level_students = 4 * sixth_level_students

    # Calculate the number of students in the seventh-level math class
    seventh_level_students = 2 * fourth_level_students

    # Calculate the total number of students
    total_students = sixth_level_students + fourth_level_students + seventh_level_students

    # return the result
    result = total_students
    return result

print(solution())