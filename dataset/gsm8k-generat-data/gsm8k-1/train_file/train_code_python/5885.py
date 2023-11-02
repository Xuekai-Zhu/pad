def solution():
    """At a middle school, 20% of the students are in the band. If 168 students are in the band, how many students go to the middle school?"""
    percent_in_band = 20
    students_in_band = 168
    total_students = students_in_band / (percent_in_band / 100)
    result = total_students
    return result

print(solution())