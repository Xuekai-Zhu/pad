def solution():
    """Carla is taking attendance for her sixth-grade class. She knows that 2 students are in the restroom, and one less than three times that number of students are absent. If there are four rows with six desks each that are all 2/3 full, how many students does Carla teach, including the ones in and out of the classroom?"""
    students_in_restroom = 2
    students_absent = 3 * students_in_restroom - 1
    desks_full = 4 * 6 * 2 / 3
    total_students = desks_full + students_in_restroom + students_absent
    result = total_students
    return result

print(solution())