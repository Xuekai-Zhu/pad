def solution():
    """Ms. Cole teaches math in three levels of classes in her school. There are four times as many students in Ms. Cole's fourth-level math class as in her sixth-level math class. The number of students in her seventh-level math class is twice that in the fourth-level math class. If Ms. Cole's sixth-level class has 40 students, how many math students does Ms. Cole teach?"""
    level_six_students = 40
    level_four_students = level_six_students * 4
    level_seven_students = level_four_students * 2
    total_students = level_six_students + level_four_students + level_seven_students
    result = total_students
    return result

print(solution())