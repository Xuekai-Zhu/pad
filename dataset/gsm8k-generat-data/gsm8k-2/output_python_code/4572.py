def solution():
    """The ratio of boys to girls in a classroom is 3:5. If there are 4 more girls than boys, how many students are in the classroom?"""
    boy_ratio = 3
    girl_ratio = 5
    girl_boy_diff = 4
    total_ratio = boy_ratio + girl_ratio
    total_students = (girl_ratio / total_ratio) * (boy_ratio + girl_boy_diff)
    result = total_students
    return result

print(solution())