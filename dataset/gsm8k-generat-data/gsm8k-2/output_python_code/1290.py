def solution():
    """There are 14 kindergartners and 24 first graders and some second graders in Ms. Watson's class. Overall Ms. Watson has 42 students. How many second graders are in Ms. Watson’s class?"""
    total_students = 42
    kindergartners = 14
    first_graders = 24
    second_graders = total_students - kindergartners - first_graders
    result = second_graders
    return result

print(solution())