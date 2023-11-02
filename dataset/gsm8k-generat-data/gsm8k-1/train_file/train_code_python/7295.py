def solution():
    """Maddy is in college for 8 semesters. She needs 120 credits to graduate. If each class is 3 credits, how many classes does she need to take per semester?"""
    semesters = 8
    total_credits = 120
    credits_per_class = 3
    classes_per_semester = total_credits / (credits_per_class * semesters)
    result = classes_per_semester
    return result

print(solution())