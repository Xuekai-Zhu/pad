def solution():
    # Number of students in the different classes
    class_4a_girls = 12
    class_4a_boys = 13
    class_4b_girls = 15
    class_4b_boys = 11
    class_5a_girls = 9
    class_5a_boys = 13
    class_5b_girls = 10
    class_5b_boys = 11

    # Total number of boys and girls in each grade
    grade_4_girls = class_4a_girls + class_4b_girls
    grade_4_boys = class_4a_boys + class_4b_boys
    grade_5_girls = class_5a_girls + class_5b_girls
    grade_5_boys = class_5a_boys + class_5b_boys

    # Total number of boys and girls competing
    total_girls = grade_4_girls + grade_5_girls
    total_boys = grade_4_boys + grade_5_boys

    # Calculate the difference between the number of boys and girls competing
    difference = total_boys - total_girls

    result = difference
    return result

print(solution())