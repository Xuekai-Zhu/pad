def solution():
    # Calculate the number of male and female students in each class
    class1_males = 17
    class1_females = 13
    class2_males = 14
    class2_females = 18
    class3_males = 15
    class3_females = 17

    # Calculate the total number of students in each class and in all classes combined
    class1_total = class1_males + class1_females
    class2_total = class2_males + class2_females
    class3_total = class3_males + class3_females
    all_classes_total = class1_total + class2_total + class3_total

    # Calculate the difference between the number of male and female students in each class and in all classes combined
    class1_diff = abs(class1_males - class1_females)
    class2_diff = abs(class2_males - class2_females)
    class3_diff = abs(class3_males - class3_females)
    all_classes_diff = abs((class1_males + class2_males + class3_males) - (class1_females + class2_females + class3_females))

    # Calculate the total number of students unable to partner with a student of the opposite gender
    unable_to_partner = (class1_diff + class2_diff + class3_diff + all_classes_diff) / 2

    result = unable_to_partner
    return result

print(solution())