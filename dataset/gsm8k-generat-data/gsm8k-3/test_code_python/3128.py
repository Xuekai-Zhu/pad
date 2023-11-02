def solution():
    """It's field trip month, and the students took six vans and four minibusses. There were 10 students on each van and 24 students on each minibus. How many students went on the field trip?"""
    # Define the number of vans and minibusses
    num_vans = 6
    num_minibusses = 4

    # Define the number of students per van and minibus
    van_capacity = 10
    minibus_capacity = 24

    # Calculate the total number of students
    total_students = num_vans * van_capacity + num_minibusses * minibus_capacity

    # Display the total number of students
    result = total_students
    return result

print(solution())