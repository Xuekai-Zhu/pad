def solution():
    """Maddy is in college for 8 semesters. She needs 120 credits to graduate. If each class is 3 credits, how many classes does she need to take per semester?"""
    # Define the total number of credits needed to graduate and the number of semesters
    total_credits = 120
    semesters = 8

    # Calculate the number of classes Maddy needs to take per semester
    classes_per_semester = total_credits / (semesters * 3)

    # Round up to the nearest class
    classes_per_semester = math.ceil(classes_per_semester)

    # return the result
    result = classes_per_semester
    return result

print(solution())