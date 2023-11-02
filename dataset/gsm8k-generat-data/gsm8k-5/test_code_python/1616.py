def solution():
    # Calculate total study time on Monday and Tuesday
    monday_time = 4
    tuesday_time = 2 * monday_time
    total_mon_tue_time = monday_time + tuesday_time

    # Calculate total study time from Wednesday to Friday
    wed_fri_time = 3 * 3

    # Calculate remaining study time
    total_time = 25
    remaining_time = total_time - total_mon_tue_time - wed_fri_time

    # Divide remaining study time evenly between Saturday and Sunday
    saturday_time = remaining_time / 2
    result = saturday_time
    return result

print(solution())