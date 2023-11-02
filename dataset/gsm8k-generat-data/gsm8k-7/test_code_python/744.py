def solution():
    yolanda_speed = 20  # miles per hour
    husband_speed = 40  # miles per hour
    time_difference = 0.25  # 15 minutes = 0.25 hours

    # Calculate the distance that Yolanda covers in the time difference
    yolanda_distance = yolanda_speed * time_difference

    # Determine how long it takes for the husband to catch up to Yolanda
    time_to_catch_up = yolanda_distance / (husband_speed - yolanda_speed)

    # Convert the time to minutes
    time_to_catch_up_minutes = time_to_catch_up * 60
    result = time_to_catch_up_minutes
    return result

print(solution())