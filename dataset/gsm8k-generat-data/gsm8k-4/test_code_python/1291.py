def solution():
    """There are 14 kindergartners and 24 first graders and some second graders in Ms. Watson's class. Overall Ms. Watson has 42 students. How many second graders are in Ms. Watson’s class?"""
    # Define the total number of students and the number of kindergarten and first grade students
    total_students = 42
    kf_students = 14
    fg_students = 24

    # Calculate the number of second grade students
    sg_students = total_students - kf_students - fg_students

    # return the result
    result = sg_students
    return result

print(solution())