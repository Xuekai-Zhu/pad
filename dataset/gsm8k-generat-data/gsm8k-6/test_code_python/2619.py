def solution():
    # Calculate the total number of people who attended class over the five days
    total_attendance = 10 + 15 + 10*3  # 10 people on Monday, 15 on Tuesday, and 10 each day from Wednesday through Friday

    # Calculate the average number of people who attended class each day
    average_attendance = total_attendance / 5
    result = average_attendance
    return result

print(solution())