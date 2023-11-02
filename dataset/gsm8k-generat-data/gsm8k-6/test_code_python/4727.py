def solution():
    # Calculate the total number of minutes the sun sets later every day
    total_later_minutes = 1.2 * 40  # the sun sets 1.2 minutes later every day for 40 days
    # Calculate the number of minutes after 6:00 PM on March 1st
    minutes_after_sunset = (6*60 + 10) - (6*60)  # it is 6:10 PM on the given day
    # Calculate the total number of minutes until sunset
    total_minutes_until_sunset = (6*60 + minutes_after_sunset) + total_later_minutes
    result = total_minutes_until_sunset
    return result

print(solution())