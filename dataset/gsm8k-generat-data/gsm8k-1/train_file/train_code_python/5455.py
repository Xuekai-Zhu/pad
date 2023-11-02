def solution():
    """There are 100 students in class and the ratio of boys to girls is 3:2. How many more boys than girls are there?"""
    total_students = 100
    boys_ratio = 3
    girls_ratio = 2
    total_ratio = boys_ratio + girls_ratio
    boys_count = (boys_ratio/total_ratio) * total_students
    girls_count = (girls_ratio/total_ratio) * total_students
    boys_diff = boys_count - girls_count
    result = boys_diff
    return result

print(solution())