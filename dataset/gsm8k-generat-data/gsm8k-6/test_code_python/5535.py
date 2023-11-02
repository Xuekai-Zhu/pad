def solution():
    # Calculate the total number of students in each class and the average class size
    class1_size = 13 + 20  # 3 and 4-year-olds in one class
    class2_size = 15 + 22  # 5 and 6-year-olds in another class
    average_class_size = (class1_size + class2_size) / 2
    result = average_class_size
    return result

print(solution())