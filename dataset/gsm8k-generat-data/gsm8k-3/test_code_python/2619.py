def solution():
    """10 people attended class on Monday, 15 on Tuesday, and 10 on each day from Wednesday through Friday. What was the average number of people who attended class each day?"""
    # Define the number of people who attended each day
    monday_attendance = 10
    tuesday_attendance = 15
    wed_fri_attendance = 10

    # Calculate the total attendance over the five days
    total_attendance = monday_attendance + tuesday_attendance + (wed_fri_attendance * 3)

    # Calculate the average attendance per day
    average_attendance = total_attendance / 5

    # Display the average attendance per day
    result = average_attendance
    return result

print(solution())