def solution():
    # Calculate the number of absent students
    restroom_students = 2  # 2 students are in the restroom
    absent_students = 3 * restroom_students - 1  # 1 less than 3 times the number of students in the restroom

    # Calculate the number of students in the classroom
    desks_per_row = 6  # There are 6 desks per row
    rows = 4  # There are 4 rows in the classroom
    capacity_per_row = desks_per_row * 2 / 3  # Each row is 2/3 full
    total_capacity = rows * capacity_per_row  # Total classroom capacity
    total_students = int(total_capacity + restroom_students - absent_students)  # Total number of students in and out of the classroom

    result = total_students
    return result

print(solution())