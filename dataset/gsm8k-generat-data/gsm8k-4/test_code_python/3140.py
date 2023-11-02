def solution():
    """There are 10 rows of 15 chairs set up for the award ceremony. The first row is reserved for the awardees while the second and third rows are for the administrators and teachers. The last two rows are then reserved for the parents and the rest of the rows are for the students. If only 4/5 of the seats reserved for the students are occupied, how many vacant seats from the students can be given to the parents?"""
    # Define the number of rows and chairs
    rows = 10
    chairs_per_row = 15

    # Define the number of chairs reserved for each group
    awardees_chairs = 15
    admin_chairs = 15 * 2
    parent_chairs = 15 * 2
    teacher_chairs = 15

    # Calculate the total number of chairs reserved
    reserved_chairs = awardees_chairs + admin_chairs + parent_chairs + teacher_chairs

    # Calculate the number of chairs for students
    student_chairs = rows * chairs_per_row - reserved_chairs

    # Calculate the number of occupied student chairs
    occupied_student_chairs = student_chairs * 4 / 5

    # Calculate the number of vacant student chairs
    vacant_student_chairs = student_chairs - occupied_student_chairs

    # Calculate the number of vacant student chairs that can be given to parents
    vacant_chairs_for_parents = vacant_student_chairs

    result = vacant_chairs_for_parents
    return result

print(solution())