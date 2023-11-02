def solution():
    # Calculate the total amount of rainfall in inches
    total_rainfall = 2 + 4*1 + 7*3  # 2 inches in the first hour, 4 hours of 1 inch per hour, 7 hours of 3 inches per hour

    # Calculate the time it takes to fill the fish tank
    time_to_fill = 18/total_rainfall * 60  # convert time to minutes
    hour = int(time_to_fill / 60) + 1  # add 1 hour to account for starting at 1 pm
    minute = int(time_to_fill % 60)

    # Format time as a string
    if hour > 12:
        hour -= 12
        suffix = 'pm'
    else:
        suffix = 'am'
    time_str = '{}:{:02d}{}'.format(hour, minute, suffix)

    result = time_str
    return result

print(solution())