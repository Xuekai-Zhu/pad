def solution():
    # Calculate the number of absent students based on the number of students in the restroom
    restroom_count = 2
    absent_count = 3 * restroom_count - 1

    # Calculate the total number of students in the class
    desks_full = 4 * 6 * (2/3)
    total_students = desks_full + restroom_count + absent_count

    result = total_students
    return result

print(solution())