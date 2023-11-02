def solution():
    """In Hawaii, they normally get an average of 2 inches of rain a day. With 100 days left in the year, they've gotten 430 inches of rain. How many inches on average do they need to finish the year with the normal average?"""
    normal_daily_inches = 2
    days_left = 100
    total_normal_inches = (365 - days_left) * normal_daily_inches
    remaining_inches = total_normal_inches - 430
    average_remaining_inches = remaining_inches / days_left
    result = average_remaining_inches
    return result

print(solution())