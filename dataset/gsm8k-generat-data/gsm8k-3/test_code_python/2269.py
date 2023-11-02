def solution():
    """ Mr. McNeely takes a register of the total number of students present in class every day.
    On a particular week, the number of students in the class on the second day was 40 more than the first day.
    The number of students who didn't turn up for the class on the second day was twice the number of students who didn't turn up on the third day.
    On the third day, 1/7 of the total number of students of the class called in sick.
    If the total number of students in the class is 280, calculate the number of absent students in the three days."""

    # Define the total number of students
    total_students = 280

    # Calculate the number of students present on the first day
    first_day = total_students / 3

    # Calculate the number of students present on the second day
    second_day = first_day + 40

    # Calculate the number of students present on the third day
    third_day = total_students - first_day - second_day

    # Calculate the number of students absent on the second day
    absent_second = 2 * absent_third

    # Calculate the number of students absent on the first day
    absent_first = total_students - first_day

    # Calculate the number of students absent on the third day
    absent_third = int(third_day / 7)

    # Calculate the total number of absent students
    total_absent = absent_first + absent_second + absent_third

    # Display the total number of absent students
    result = total_absent
    return result

print(solution())