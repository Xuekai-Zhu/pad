def solution():
    """Maddy is in college for 8 semesters. She needs 120 credits to graduate. If each class is 3 credits, how many classes does she need to take per semester?"""
    # Define the number of semesters and credits needed to graduate
    semesters = 8
    credits_needed = 120

    # Calculate the total number of classes needed to graduate
    classes_needed = credits_needed / 3

    # Calculate the number of classes needed per semester
    classes_per_semester = classes_needed / semesters

    # Display the number of classes needed per semester
    result = classes_per_semester
    return result

print(solution())