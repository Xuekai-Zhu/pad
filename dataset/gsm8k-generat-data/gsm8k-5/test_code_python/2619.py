def solution():
    # Calculate the total number of people who attended class
    total_attendance = 10 + 15 + (10 * 3)  # 10 on Monday, 15 on Tuesday, 10 each on Wednesday through Friday

    # Calculate the total number of days
    total_days = 5  # Monday through Friday

    # Calculate the average number of people who attended class each day
    average_attendance = total_attendance / total_days
    result = average_attendance
    return result

print(solution())