def solution():
    # Calculate the total number of boys and girls
    total_ratio = 3 + 2
    total_students = 100
    boys = (3 / total_ratio) * total_students
    girls = (2 / total_ratio) * total_students

    # Calculate the difference between the number of boys and girls
    difference = boys - girls
    result = difference
    return result

print(solution())