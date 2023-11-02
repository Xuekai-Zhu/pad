def solution():
    total_students = 100  # There are 100 students in class
    boys_ratio = 3 / 5  # The ratio of boys to girls is 3:2
    girls_ratio = 2 / 5

    # Calculate the number of boys and girls
    total_ratio = boys_ratio + girls_ratio
    boys = total_students * boys_ratio / total_ratio
    girls = total_students * girls_ratio / total_ratio

    # Calculate the difference between the number of boys and girls
    difference = boys - girls
    result = difference
    return result

print(solution())