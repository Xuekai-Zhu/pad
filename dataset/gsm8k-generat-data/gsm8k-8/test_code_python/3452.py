def solution():
    max_screen_time = 120 # in minutes
    morning_screen_time = 45 # in minutes

    # Calculate the remaining screen time for the evening
    remaining_screen_time = max_screen_time - morning_screen_time

    # Convert remaining screen time from minutes to hours and minutes
    hours = remaining_screen_time // 60
    minutes = remaining_screen_time % 60

    # Format the result as a string
    result = "{} hours and {} minutes".format(hours, minutes)
    return result

print(solution())