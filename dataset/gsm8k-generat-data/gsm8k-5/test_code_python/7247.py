def solution():
    total_attendance = 2700  # Total attendance for all three days combined
    first_day_attendance = total_attendance / 5  # Assume that the first day had 5 times the attendance of the second day
    third_day_attendance = first_day_attendance * 3  # Attendance on the third day was triple that of the first day
    second_day_attendance = total_attendance - first_day_attendance - third_day_attendance  # Calculate attendance on the second day
    result = second_day_attendance
    return result

print(solution())