def solution():
    """Musa is the class teacher of a class of 45 students. He wants to split them into three groups by age. If a third of the class is under 11 years, and two-fifths are above 11 but under 13, how many students will be in the third group (13 years and above)?"""
    total_students = 45
    under_11 = total_students // 3
    above_11_below_13 = (2 / 5) * total_students
    above_13 = total_students - under_11 - above_11_below_13
    result = above_13
    return result

print(solution())