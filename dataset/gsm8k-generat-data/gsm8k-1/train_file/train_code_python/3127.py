def solution():
    """It's field trip month, and the students took six vans and four minibusses. There were 10 students on each van and 24 students on each minibus. How many students went on the field trip?"""
    vans = 6
    minibusses = 4
    students_per_van = 10
    students_per_minibus = 24
    total_students = (vans * students_per_van) + (minibusses * students_per_minibus)
    result = total_students
    return result

print(solution())