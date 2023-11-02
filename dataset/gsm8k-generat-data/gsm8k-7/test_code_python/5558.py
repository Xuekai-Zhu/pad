def solution():
    total_ratio = 5 + 8  # total ratio of boys and girls
    total_students = 260  # total number of students in the class

    # Calculate the fraction of the ratio that represents girls
    girl_fraction = 8 / total_ratio

    # Calculate the number of girls in the class
    num_girls = girl_fraction * total_students

    result = num_girls
    return result

print(solution())