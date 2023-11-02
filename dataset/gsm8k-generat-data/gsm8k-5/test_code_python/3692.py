def solution():
    class1_males = 17
    class1_females = 13
    class2_males = 14
    class2_females = 18
    class3_males = 15
    class3_females = 17

    # Determine the minimum number of students that can't partner with someone of the opposite gender
    min_unmatched = min((class1_males - class1_females), (class2_males - class2_females), (class3_males - class3_females))

    # Calculate the total number of students
    total_students = class1_males + class1_females + class2_males + class2_females + class3_males + class3_females

    # Calculate the number of students that can't partner with someone of the opposite gender
    num_unmatched = (class1_males - class1_females) + (class2_males - class2_females) + (class3_males - class3_females)

    # If it's not possible for each male to partner with a female, then all of the unmatched students won't be able to partner
    if (total_students % 2 != 0) or (num_unmatched > total_students / 2):
        result = total_students - (total_students // 2) * 2
    else:
        result = num_unmatched - min_unmatched
    return result

print(solution())