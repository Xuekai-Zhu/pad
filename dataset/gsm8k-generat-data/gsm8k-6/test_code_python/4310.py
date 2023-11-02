def solution():
    # Calculate the number of students present in the science class today
    present_today = (0.9 * 2 * 70) - 30  # 10% less than twice the total number of students present yesterday minus 30 absent today

    # Calculate the total number of students registered for the course
    total_registered = present_today + 30  # add 30 absent students to the present students
    result = total_registered
    return result

print(solution())