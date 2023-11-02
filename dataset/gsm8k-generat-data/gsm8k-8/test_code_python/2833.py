def solution():
    # Calculate the number of students who prefer goldfish in each class
    class1 = 30 * (1/6)
    class2 = 30 * (2/3)
    class3 = 30 * (1/5)

    # Calculate the total number of students who prefer goldfish
    total_goldfish = class1 + class2 + class3
    result = total_goldfish
    return result

print(solution())