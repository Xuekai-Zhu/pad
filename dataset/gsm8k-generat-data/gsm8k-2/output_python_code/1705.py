def solution():
    """There are 400 students in the senior class at East High School. 52% of the students play sports. Of the students that play sports, 12.5% play soccer. How many students play soccer?"""
    total_students = 400
    sports_percent = 0.52
    soccer_percent = 0.125
    sports_students = total_students * sports_percent
    soccer_students = sports_students * soccer_percent
    result = soccer_students
    return result

print(solution())