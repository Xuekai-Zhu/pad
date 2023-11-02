def solution():
    """In today's field day challenge, the 4th graders were competing against the 5th graders. Each grade had 2 different classes. The first 4th grade class had 12 girls and 13 boys. The second 4th grade class had 15 girls and 11 boys. The first 5th grade class had 9 girls and 13 boys while the second 5th grade class had 10 girls and 11 boys. In total, how many more boys were competing than girls?"""
    # Define the number of girls and boys in each class
    class_4a_g = 12
    class_4a_b = 13
    class_4b_g = 15
    class_4b_b = 11
    class_5a_g = 9
    class_5a_b = 13
    class_5b_g = 10
    class_5b_b = 11

    # Calculate the total number of girls and boys competing
    total_girls = class_4a_g + class_4b_g + class_5a_g + class_5b_g
    total_boys = class_4a_b + class_4b_b + class_5a_b + class_5b_b

    # Calculate the difference between the number of boys and girls
    difference = total_boys - total_girls

    # return the result
    result = difference
    return result

print(solution())