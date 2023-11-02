def solution():
    """The ratio of boys to girls in a math class is 5:8. How many girls are in the class if the total number of students in the class is 260?"""
    total_students = 260
    ratio = 5/8
    girls = total_students / (1 + ratio)
    result = girls
    return result

print(solution())