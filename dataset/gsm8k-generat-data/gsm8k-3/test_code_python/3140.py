def solution():
    """There are 10 rows of 15 chairs set up for the award ceremony. The first row is reserved for the awardees while the second and third rows are for the administrators and teachers. The last two rows are then reserved for the parents and the rest of the rows are for the students. If only 4/5 of the seats reserved for the students are occupied, how many vacant seats from the students can be given to the parents?"""

    # Define the number of chairs per row and the number of rows for each group
    CHAIRS_PER_ROW = 15
    AWARDEE_ROWS = 1
    ADMIN_TEACHER_ROWS = 2
    PARENT_ROWS = 2
    STUDENT_ROWS = 10 - AWARDEE_ROWS - ADMIN_TEACHER_ROWS - PARENT_ROWS

    # Calculate the total number of chairs
    total_chairs = CHAIRS_PER_ROW * 10

    # Calculate the number of chairs reserved for the awardees, administrators, and teachers
    reserved_chairs = CHAIRS_PER_ROW * (AWARDEE_ROWS + ADMIN_TEACHER_ROWS)

    # Calculate the number of chairs reserved for the parents
    parent_chairs = CHAIRS_PER_ROW * PARENT_ROWS

    # Calculate the number of chairs reserved for the students
    student_chairs = total_chairs - reserved_chairs - parent_chairs

    # Calculate the number of occupied student chairs
    occupied_student_chairs = int(student_chairs * 4/5)

    # Calculate the number of vacant student chairs that can be given to the parents
    vacant_student_chairs = student_chairs - occupied_student_chairs

    # Display the number of vacant student chairs that can be given to the parents
    result = vacant_student_chairs
    return result

print(solution())