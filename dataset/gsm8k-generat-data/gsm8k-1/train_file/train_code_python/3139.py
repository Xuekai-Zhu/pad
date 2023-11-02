def solution():
    """There are 10 rows of 15 chairs set up for the award ceremony. The first row is reserved for the awardees while the second and third rows are for the administrators and teachers. The last two rows are then reserved for the parents and the rest of the rows are for the students. If only 4/5 of the seats reserved for the students are occupied, how many vacant seats from the students can be given to the parents?"""
    total_chairs = 10 * 15
    awardee_chairs = 15
    admin_chairs = 2 * 15
    teacher_chairs = 2 * 15
    parent_chairs = 2 * 15
    student_chairs = total_chairs - (awardee_chairs + admin_chairs + teacher_chairs + parent_chairs)
    occupied_student_chairs = int(student_chairs * 4/5)
    empty_student_chairs = student_chairs - occupied_student_chairs
    vacant_seats_for_parents = int(empty_student_chairs/2)
    result = vacant_seats_for_parents
    return result

print(solution())