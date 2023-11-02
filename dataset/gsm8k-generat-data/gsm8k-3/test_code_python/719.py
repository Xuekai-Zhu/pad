def solution():
    """Jenny's local library received 50 visitors on Monday. On Tuesday, the library received twice that number. On the remaining days of the week, an average of 20 visitors went to the library. What's the total number of visitors who went to the library that week?"""
    # Define the number of visitors on Monday and Tuesday
    MONDAY_VISITORS = 50
    TUESDAY_VISITORS = 2 * MONDAY_VISITORS

    # Define the average number of visitors on the remaining days of the week
    REMAINING_VISITORS = 20

    # Calculate the total number of visitors
    total_visitors = MONDAY_VISITORS + TUESDAY_VISITORS + (5 * REMAINING_VISITORS)

    # Display the total number of visitors
    result = total_visitors
    return result

print(solution())