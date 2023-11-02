def solution():
    # Calculate the total number of chairs in the room
    total_chairs = 10 * 15

    # Calculate the number of chairs reserved for awardees, administrators, and teachers
    reserved_chairs = 15 + 2 * 15

    # Calculate the number of chairs reserved for parents
    parent_chairs = 2 * 15

    # Calculate the number of chairs reserved for students
    student_chairs = total_chairs - reserved_chairs - parent_chairs

    # Calculate the number of occupied chairs for students
    occupied_student_chairs = (4 / 5) * student_chairs

    # Calculate the number of vacant chairs for students
    vacant_student_chairs = student_chairs - occupied_student_chairs

    # Calculate the number of vacant chairs that can be given to parents
    parent_vacant_chairs = min(vacant_student_chairs, parent_chairs)

    result = parent_vacant_chairs
    return result

print(solution())