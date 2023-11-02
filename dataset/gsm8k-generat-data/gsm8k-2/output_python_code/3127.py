def solution():
    """It's field trip month, and the students took six vans and four minibusses. There were 10 students on each van and 24 students on each minibus. How many students went on the field trip?"""
    van_capacity = 10
    minibus_capacity = 24
    num_vans = 6
    num_minibusses = 4
    total_students = (van_capacity * num_vans) + (minibus_capacity * num_minibusses)
    result = total_students
    return result

print(solution())