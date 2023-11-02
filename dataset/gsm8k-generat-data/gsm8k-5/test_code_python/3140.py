def solution():
    total_rows = 10  # There are 10 rows of chairs
    chairs_per_row = 15  # There are 15 chairs in each row
    rows_for_awardee = 1  # The first row is reserved for awardees
    rows_for_admin_and_teacher = 2  # The second and third rows are for administrators and teachers
    rows_for_parents = 2  # The last two rows are reserved for parents
    rows_for_students = total_rows - (rows_for_awardee + rows_for_admin_and_teacher + rows_for_parents)  # The rest of the rows are for students
    seats_reserved_for_students = rows_for_students * chairs_per_row  # Calculate the total seats reserved for students
    occupied_seats_for_students = seats_reserved_for_students * (4/5)  # Calculate the number of occupied seats for students
    vacant_seats_for_students = seats_reserved_for_students - occupied_seats_for_students  # Calculate the number of vacant seats for students
    vacant_seats_for_parents = (vacant_seats_for_students // 2)  # Divide the vacant seats equally between the two parent rows
    result = vacant_seats_for_parents
    return result

print(solution())