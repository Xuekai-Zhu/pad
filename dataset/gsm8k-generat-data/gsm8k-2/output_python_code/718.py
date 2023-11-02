def solution():
    """Jenny's local library received 50 visitors on Monday. On Tuesday, the library received twice that number. On the remaining days of the week, an average of 20 visitors went to the library. What's the total number of visitors who went to the library that week?"""
    monday_visitors = 50
    tuesday_visitors = 2 * monday_visitors
    remaining_days_visitors = 20 * 5 # assuming there are 5 remaining days
    total_visitors = monday_visitors + tuesday_visitors + remaining_days_visitors
    result = total_visitors
    return result

print(solution())