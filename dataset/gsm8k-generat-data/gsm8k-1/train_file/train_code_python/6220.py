def solution():
    """Calculate the total number of students at the science fair competition"""
    know_it_all = 50
    karen_high = (3/5) * know_it_all
    novel_corona = 2 * (know_it_all + karen_high)
    total_students = know_it_all + karen_high + novel_corona
    result = total_students
    return result

print(solution())