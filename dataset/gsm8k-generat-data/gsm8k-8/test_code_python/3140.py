def solution():
    # Calculate the total number of chairs
    total_chairs = 10 * 15

    # Calculate the number of chairs reserved for the awardees, administrators, and teachers
    reserved_chairs = 15 + (2 * 15)

    # Calculate the number of chairs reserved for the parents
    parent_chairs = 2 * 15

    # Calculate the number of chairs reserved for the students
    student_chairs = total_chairs - reserved_chairs - parent_chairs

    # Calculate the number of occupied student chairs
    occupied_student_chairs = 4/5 * student_chairs

    # Calculate the number of vacant student chairs
    vacant_student_chairs = student_chairs - occupied_student_chairs

    # Calculate the number of vacant student chairs that can be given to the parents
    vacant_chairs_for_parents = min(vacant_student_chairs, parent_chairs)

    result = vacant_chairs_for_parents
    return result

print(solution())