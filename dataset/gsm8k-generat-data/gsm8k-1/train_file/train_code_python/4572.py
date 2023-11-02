def solution():
    """The ratio of boys to girls in a classroom is 3:5. If there are 4 more girls than boys, how many students are in the classroom?"""
    boy_ratio = 3
    girl_ratio = 5
    total_ratio = boy_ratio + girl_ratio
    difference = girl_ratio - boy_ratio
    extra_girls = 4
    boy_count = (difference / total_ratio) * (extra_girls + girl_ratio)
    girl_count = girl_ratio / total_ratio * (extra_girls + girl_ratio)
    total_students = boy_count + girl_count
    result = total_students
    return result

print(solution())