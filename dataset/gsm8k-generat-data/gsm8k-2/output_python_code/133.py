def solution():
    """There are 40 students in a class. If 1/10 are absent, 3/4 of the students who are present are in the classroom, and the rest are in the canteen, how many students are in the canteen?"""
    total_students = 40
    absent_students = total_students / 10
    present_students = total_students - absent_students
    classroom_students = present_students * (3 / 4)
    canteen_students = present_students - classroom_students
    result = canteen_students
    return result

print(solution())