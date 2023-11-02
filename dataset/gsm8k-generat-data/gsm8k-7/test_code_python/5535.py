def solution():
    num_3yearolds = 13
    num_4yearolds = 20
    num_5yearolds = 15
    num_6yearolds = 22

    # Calculate the total number of students in each class
    class1_total = num_3yearolds + num_4yearolds
    class2_total = num_5yearolds + num_6yearolds

    # Calculate the average class size
    class1_size = class1_total / 2
    class2_size = class2_total / 2
    average_class_size = (class1_size + class2_size) / 2
    result = average_class_size
    return result

print(solution())