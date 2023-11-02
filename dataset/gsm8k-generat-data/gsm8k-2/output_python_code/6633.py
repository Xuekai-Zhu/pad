def solution():
    """If 60% of the students at school are girls and the number of boys is 300, how many girls are at the school?"""
    boys = 300
    girl_percentage = 60
    total_students = boys / (100 - girl_percentage) * 100
    girls = total_students - boys
    result = girls
    return result

print(solution())