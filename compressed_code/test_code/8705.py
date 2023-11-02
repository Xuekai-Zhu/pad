def solution():
    
    class1_males = 17
    class1_females = 13
    class2_males = 14
    class2_females = 18
    class3_males = 15
    class3_females = 17
    total_males = class1_males + class2_males + class3_males
    total_females = class1_females + class2_females + class3_females
    if total_males >= total_females:
        unpartnered_students = total_males - total_females
    else:
        unpartnered_students = total_females - total_males
    result = unpartnered_students
    return result

print(solution())