def solution():
    """Ms. Cole teaches math in three levels of classes in her school. There are four times as many students in Ms. Cole's fourth-level math class as in her sixth-level math class. The number of students in her seventh-level math class is twice that in the fourth-level math class. If Ms. Cole's sixth-level class has 40 students, how many math students does Ms. Cole teach?"""
    sixth_level = 40
    fourth_level = 4 * sixth_level
    seventh_level = 2*fourth_level
    total_students = sixth_level + fourth_level + seventh_level
    result = total_students
    return result

print(solution())