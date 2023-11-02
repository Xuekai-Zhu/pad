def solution():
    """Three different 6th grade classes are combining for a square dancing unit. If possible, the teachers would like each male student to partner with a female student for the unit. The first class has 17 males and 13 females, while the second class has 14 males and 18 females, and the third class has 15 males and 17 females. When the classes are combined, how many students will be unable to partner with a student of the opposite gender?"""
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