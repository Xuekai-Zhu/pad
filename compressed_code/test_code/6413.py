def solution():
    
    students_in_bathroom = 2
    students_absent = 3 * students_in_bathroom - 1
    desks_per_row = 6
    rows = 4
    desk_occupancy = 2 / 3
    total_desks = desks_per_row * rows
    students_in_classroom = round(total_desks * desk_occupancy)
    total_students = students_in_classroom + students_in_bathroom + students_absent
    result = total_students
    return result

print(solution())