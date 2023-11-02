def solution():
    # Initial enrollment
    enrollment = 8

    # New students from advertising
    new_students = 8
    new_students_dropped = new_students / 4
    enrollment += new_students - new_students_dropped

    # Two students leave
    enrollment -= 2

    # Enrollment increases by 5 times
    enrollment *= 5
    enrollment -= 2

    # Six more students enroll
    enrollment += 6

    # Half of the class drops out
    enrollment /= 2

    # Half of remaining students graduate
    enrollment /= 2

    result = enrollment
    return result

print(solution())