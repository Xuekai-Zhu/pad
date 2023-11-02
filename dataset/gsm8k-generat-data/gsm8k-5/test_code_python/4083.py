def solution():
    normal_average = 2  # Hawaii normally gets an average of 2 inches of rain a day
    total_days = 365  # There are 365 days in a year
    days_left = 100  # There are 100 days left in the year
    current_rain = 430  # They've already gotten 430 inches of rain

    # Calculate the total amount of rain they should have gotten by now
    normal_rain = normal_average * (total_days - days_left)

    # Calculate the amount of rain they still need to get to reach the normal average
    needed_rain = normal_rain - current_rain

    # Calculate the average amount of rain they need for the remaining 100 days
    average_needed = needed_rain / days_left
    result = average_needed
    return result

print(solution())