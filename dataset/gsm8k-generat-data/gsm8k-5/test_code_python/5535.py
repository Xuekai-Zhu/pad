def solution():
    # Calculate the total number of students in each class
    class1_total = 13 + 20  # 3 and 4-year-olds in one class
    class2_total = 15 + 22  # 5 and 6-year-olds in another class

    # Calculate the average class size
    average_class_size = (class1_total + class2_total) / 2
    result = average_class_size
    return result

print(solution())