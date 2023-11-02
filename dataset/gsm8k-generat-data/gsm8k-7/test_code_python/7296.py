def solution():
    num_semesters = 8
    num_credits = 120
    credits_per_class = 3

    # Calculate the total number of classes that Maddy needs to take
    total_classes = num_credits / credits_per_class

    # Calculate the number of classes Maddy needs to take per semester
    classes_per_semester = total_classes / num_semesters
    result = classes_per_semester
    return result

print(solution())