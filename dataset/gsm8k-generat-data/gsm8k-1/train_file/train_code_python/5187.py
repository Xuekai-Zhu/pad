def solution():
    """There are 325 students in a local high school. 40 percent of the students have glasses, how many students do not have glasses?"""
    total_students = 325
    glasses_percent = 40
    glasses_students = total_students * (glasses_percent / 100)
    no_glasses_students = total_students - glasses_students
    result = no_glasses_students
    return result

print(solution())