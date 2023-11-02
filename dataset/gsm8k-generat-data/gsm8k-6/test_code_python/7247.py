def solution():
    # Calculate the number of people who attended each day
    first_day = x  # let x be the number of people who attended the first day
    second_day = 0.5 * first_day  # half the number of people who attended the first day showed up the second day
    third_day = 3 * first_day  # attendance on the third day was triple the attendance on the first day
    total_attendance = 2700  # total attendance for the three days

    # Use the information above to solve for the value of x
    x = total_attendance / (1 + 0.5 + 3)

    # Calculate the attendance on the second day
    attendance_second_day = 0.5 * x
    result = attendance_second_day
    return result

print(solution())