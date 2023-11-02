def solution():
    total_students = 100
    girl_students = 40
    boy_students = total_students - girl_students
    monitors = 8
    students_per_monitor = 15
    monitor_ratio = monitors / students_per_monitor
    cartons_per_boy = 1
    cartons_per_girl = 2
    total_cartons = (cartons_per_boy * boy_students) + (cartons_per_girl * girl_students)
    result = total_cartons
    return result

print(solution())