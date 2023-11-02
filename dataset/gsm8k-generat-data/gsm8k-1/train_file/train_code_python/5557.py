def solution():
    """The ratio of boys to girls in a math class is 5:8. How many girls are in the class if the total number of students in the class is 260?"""
    total_students = 260
    ratio_boys = 5
    ratio_girls = 8
    total_ratio = ratio_boys + ratio_girls
    girls_ratio = ratio_girls / total_ratio
    girls_in_class = girls_ratio * total_students
    result = girls_in_class
    return result

print(solution())