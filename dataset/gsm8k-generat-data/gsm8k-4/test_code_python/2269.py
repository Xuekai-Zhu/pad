def solution():
    """Mr. McNeely takes a register of the total number of students present in class every day. On a particular week, the number of students in the class on the second day was 40 more than the first day. The number of students who didn't turn up for the class on the second day was twice the number of students who didn't turn up on the third day. On the third day, 1/7 of the total number of students of the class called in sick. If the total number of students in the class is 280, calculate the number of absent students in the three days."""
    # Define the total number of students in the class
    total_students = 280

    # Calculate the number of students present on the third day
    third_day_students = total_students / (1 + 1/7)

    # Calculate the number of absent students on the third day
    third_day_absent = total_students - third_day_students

    # Calculate the number of absent students on the second day
    second_day_absent = 2 * third_day_absent

    # Calculate the number of present students on the first day
    first_day_students = total_students - third_day_absent - second_day_absent - 40

    # Calculate the number of absent students on the first day
    first_day_absent = total_students - first_day_students

    # Calculate the total number of absent students in the three days
    total_absent = first_day_absent + second_day_absent + third_day_absent

    result = total_absent
    return result

print(solution())