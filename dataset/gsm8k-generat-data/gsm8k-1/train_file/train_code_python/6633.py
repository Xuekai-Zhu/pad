def solution():
    """If 60% of the students at school are girls and the number of boys is 300, how many girls are at the school?"""
    total_students = 100
    boys_percent = 40
    boys_num = 300
    girls_percent = total_students - boys_percent
    girls_num = (girls_percent / 100) * (boys_num / (boys_percent / 100))
    result = girls_num
    return result

print(solution())