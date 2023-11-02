def solution():
    num_rows = 10
    chairs_per_row = 15

    # Calculate the total number of chairs in the room
    total_chairs = num_rows * chairs_per_row

    # Calculate the number of chairs reserved for awardees, administrators, teachers, and parents
    reserved_chairs = chairs_per_row + (2 * chairs_per_row) + (2 * chairs_per_row)

    # Calculate the number of chairs reserved for students
    student_chairs = total_chairs - reserved_chairs

    # Calculate the number of occupied student chairs
    occupied_student_chairs = (4/5) * student_chairs

    # Calculate the number of vacant student chairs that can be given to parents
    vacant_student_chairs = student_chairs - occupied_student_chairs - (2 * chairs_per_row)

    result = vacant_student_chairs
    return result

print(solution())