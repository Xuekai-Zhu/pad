def solution():
    students_in_class = 10
    classes = 2
    students_on_trip = students_in_class * classes
    parents = 5
    teachers = 2
    students_going_home = 10
    chaperones_going_home = 2
    total_left = students_on_trip + parents + teachers - students_going_home - chaperones_going_home
    result = total_left
    return result

print(solution())