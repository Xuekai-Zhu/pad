def solution():
    """In Hawaii, they normally get an average of 2 inches of rain a day. With 100 days left in the year, they've gotten 430 inches of rain. How many inches on average do they need to finish the year with the normal average?"""
    normal_average = 2
    days_left = 100
    total_rain = 430
    remaining_rain_needed = (normal_average * (365 - days_left)) - total_rain
    average_rain_needed = remaining_rain_needed / days_left
    result = average_rain_needed
    return result

print(solution())