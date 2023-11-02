def solution():
    total_students = 280

    # Calculate number of students on first and second day
    second_day = first_day + 40
    first_day = total_students / 3

    # Calculate number of absent students on third day
    third_day = total_students - first_day - second_day
    third_day_sick = third_day / 7
    third_day_absent = third_day - third_day_sick

    # Calculate number of absent students on first and second day
    second_day_absent = 2 * third_day_absent
    first_day_absent = total_students - second_day - third_day - second_day_absent

    # Calculate total number of absent students
    total_absent = first_day_absent + second_day_absent + third_day_absent

    result = total_absent
    return result

print(solution())