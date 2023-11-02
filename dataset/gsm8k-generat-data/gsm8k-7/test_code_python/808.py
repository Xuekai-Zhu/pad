def solution():
    num_students_in_restroom = 2
    num_absent_students = 3*num_students_in_restroom - 1
    num_desks_per_row = 6
    fraction_of_desks_filled = 2/3
    num_rows = 4

    # Calculate the total number of desks in the classroom
    total_num_desks = num_rows * num_desks_per_row

    # Calculate the total number of students who are present
    num_students_present = (total_num_desks * fraction_of_desks_filled) - num_students_in_restroom

    # Calculate the total number of students Carla teaches, including absent students
    total_num_students = num_students_present + num_absent_students
    result = total_num_students
    return result

print(solution())