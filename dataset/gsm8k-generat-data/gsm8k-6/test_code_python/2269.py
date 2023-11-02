def solution():
    # Calculate the number of students present on the third day
    third_day_absent = (1/7) * 280  # 1/7 of the total number of students called in sick
    third_day_present = 280 - third_day_absent  # calculate the number of students present

    # Calculate the number of students present on the second day
    second_day_present = third_day_present + 40  # The number of students in class on the second day was 40 more than the first day

    # Calculate the number of absent students on the second day
    second_day_absent = 2 * (third_day_absent - (second_day_present - third_day_present))

    # Calculate the total number of absent students
    total_absent = second_day_absent + third_day_absent + 0  # the first day had no absent students

    result = total_absent
    return result

print(solution())