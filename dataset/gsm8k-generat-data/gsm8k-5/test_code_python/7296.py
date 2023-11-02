def solution():
    total_semesters = 8  # Maddy is in college for 8 semesters
    credits_needed = 120  # Maddy needs 120 credits to graduate
    credits_per_class = 3  # Each class is worth 3 credits

    # Calculate the total number of classes Maddy needs to take
    total_classes = credits_needed / credits_per_class

    # Calculate the number of classes Maddy needs to take per semester
    classes_per_semester = total_classes / total_semesters
    result = classes_per_semester
    return result

print(solution())