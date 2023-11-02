def solution():
    total_attendance = 2700
    first_day_attendance = total_attendance / 7  # Assume 1/7 of total attendance on first day
    second_day_attendance = first_day_attendance / 2
    third_day_attendance = first_day_attendance * 3

    # Calculate the total attendance for the three days
    total_day_attendance = first_day_attendance + second_day_attendance + third_day_attendance

    # Calculate the attendance for the second day
    second_day_attendance = total_attendance - total_day_attendance + second_day_attendance
    result = second_day_attendance
    return result

print(solution())