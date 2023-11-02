def solution():
    """10 people attended class on Monday, 15 on Tuesday, and 10 on each day from Wednesday through Friday. What was the average number of people who attended class each day?"""
    total_people = 10 + 15 + 10 + 10 + 10 + 10
    days_attended = 6
    average_attendance = total_people / days_attended
    result = average_attendance
    return result

print(solution())