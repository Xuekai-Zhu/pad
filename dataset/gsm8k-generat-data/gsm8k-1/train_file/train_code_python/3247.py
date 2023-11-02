def solution():
    """There are 180 students in ninth grade. 1/4 of them bombed their finals because they were going through difficult breakups. 1/3rd of the rest didn't show up to take the test, and another 20 got less than a D. How many students passed their finals?"""
    total_students = 180
    bombed = total_students // 4
    remaining_students = total_students - bombed
    didnt_show_up = remaining_students // 3
    less_than_d = 20
    passed = total_students - bombed - didnt_show_up - less_than_d
    result = passed
    return result

print(solution())