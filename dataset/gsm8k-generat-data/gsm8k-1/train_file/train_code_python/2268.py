def solution():
    """Mr. McNeely takes a register of the total number of students present in class every day. On a particular week, the number of students in the class on the second day was 40 more than the first day. The number of students who didn't turn up for the class on the second day was twice the number of students who didn't turn up on the third day. On the third day, 1/7 of the total number of students of the class called in sick. If the total number of students in the class is 280, calculate the number of absent students in the three days."""
    total_students = 280
    first_day = total_students / 3
    second_day = first_day + 40
    third_day_sick = total_students / 7
    third_day_absent = (second_day - first_day) / 2
    total_absent = first_day + second_day + third_day_absent + third_day_sick - total_students
    result = total_absent
    return result

print(solution())