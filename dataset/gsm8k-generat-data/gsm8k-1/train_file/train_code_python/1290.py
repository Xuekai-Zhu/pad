def solution():
    """There are 14 kindergartners and 24 first graders and some second graders in Ms. Watson's class. Overall Ms. Watson has 42 students. How many second graders are in Ms. Watson’s class?"""
    total_students = 42
    first_grade = 24
    kindergarten = 14
    second_grade = total_students - first_grade - kindergarten
    result = second_grade
    return result

print(solution())