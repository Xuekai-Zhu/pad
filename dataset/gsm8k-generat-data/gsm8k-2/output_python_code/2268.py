def solution():
    """Mr. McNeely takes a register of the total number of students present in class every day. On a particular week, the number of students in the class on the second day was 40 more than the first day. The number of students who didn't turn up for the class on the second day was twice the number of students who didn't turn up on the third day. On the third day, 1/7 of the total number of students of the class called in sick. If the total number of students in the class is 280, calculate the number of absent students in the three days."""
    total_students = 280
    third_day_sick_students = total_students // 7
    second_day_present_students = total_students - third_day_sick_students
    first_day_present_students = second_day_present_students - 40
    second_day_absent_students = 2 * (total_students - second_day_present_students)
    third_day_absent_students = total_students - (third_day_sick_students + second_day_absent_students + second_day_present_students)
    total_absent_students = first_day_present_students + second_day_absent_students + third_day_absent_students
    result = total_absent_students
    return result

print(solution())