def solution():
    """There are 32 students in a statistics course. 25 percent of the class received an A. 1/4 of the remaining students got either a B or C, and the rest of the students failed. How many students failed?"""
    total_students = 32
    a_students = total_students * 0.25
    remaining_students = total_students - a_students
    b_or_c_students = remaining_students / 4
    failed_students = total_students - a_students - b_or_c_students
    result = failed_students
    return result

print(solution())