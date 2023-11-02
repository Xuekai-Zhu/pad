def solution():
    """Five coaster vans are used to transport students for their field trip. Each van carries 28 students, 60 of which are boys. How many are girls?"""
    # Define the number of students per van and the total number of vans
    STUDENTS_PER_VAN = 28
    TOTAL_VANS = 5

    # Calculate the total number of students
    total_students = STUDENTS_PER_VAN * TOTAL_VANS

    # Calculate the number of girls
    girls = total_students - 60

    # return the result
    result = girls
    return result

print(solution())