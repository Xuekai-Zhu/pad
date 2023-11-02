def solution():
    total_students = 280
    first_day = total_students / 3

    # Calculate the number of students on the second day using the information provided
    second_day = first_day + 40
    # Calculate the number of absent students on the second day
    absent_on_second_day = 2 * (total_students - first_day - second_day)

    # Calculate the number of sick students on the third day
    sick_on_third_day = total_students / 7

    # Calculate the number of absent students on the third day
    absent_on_third_day = total_students - (first_day + second_day + sick_on_third_day)

    # Calculate the total number of absent students for the three days
    total_absent = absent_on_second_day + absent_on_third_day

    result = total_absent
    return result

print(solution())