def solution():
    """Carla is taking attendance for her sixth-grade class. She knows that 2 students are in the restroom, and one less than three times that number of students are absent. If there are four rows with six desks each that are all 2/3 full, how many students does Carla teach, including the ones in and out of the classroom?"""
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