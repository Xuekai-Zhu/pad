def solution():
    """There are 180 students in ninth grade. 1/4 of them bombed their finals because they were going through difficult breakups. 1/3rd of the rest didn't show up to take the test, and another 20 got less than a D. How many students passed their finals?"""
    total_students = 180
    bombed_students = total_students // 4
    remaining_students = total_students - bombed_students
    skipped_students = remaining_students // 3
    low_grade_students = 20
    passed_students = total_students - (bombed_students + skipped_students + low_grade_students)
    result = passed_students
    return result

print(solution())