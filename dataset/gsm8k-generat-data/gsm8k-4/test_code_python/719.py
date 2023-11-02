def solution():
    """Jenny's local library received 50 visitors on Monday. On Tuesday, the library received twice that number. On the remaining days of the week, an average of 20 visitors went to the library. What's the total number of visitors who went to the library that week?"""
    # Define the number of visitors on Monday and Tuesday
    monday_visitors = 50
    tuesday_visitors = monday_visitors * 2

    # Define the average number of visitors on the remaining days of the week
    remaining_days_visitors = 20

    # Calculate the total number of visitors
    total_visitors = monday_visitors + tuesday_visitors + (remaining_days_visitors * 5)

    result = total_visitors
    return result

print(solution())