def solution():
    """It's field trip month, and the students took six vans and four minibusses. There were 10 students on each van and 24 students on each minibus. How many students went on the field trip?"""
    # Define the number of vans and minibuses
    vans = 6
    minibuses = 4

    # Define the number of students on each van and minibus
    van_students = 10
    minibus_students = 24

    # Calculate the total number of students on the field trip
    total_students = (vans * van_students) + (minibuses * minibus_students)

    # Return the result
    result = total_students
    return result

print(solution())