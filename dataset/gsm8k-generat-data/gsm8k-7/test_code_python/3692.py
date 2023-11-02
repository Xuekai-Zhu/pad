def solution():
    # Number of males and females in each class
    class1_males = 17
    class1_females = 13

    class2_males = 14
    class2_females = 18

    class3_males = 15
    class3_females = 17

    # Total number of males and females
    total_males = class1_males + class2_males + class3_males
    total_females = class1_females + class2_females + class3_females

    # Determine if each male can be paired with a female
    num_unpaired = max(total_males, total_females) - min(total_males, total_females)

    result = num_unpaired
    return result

print(solution())