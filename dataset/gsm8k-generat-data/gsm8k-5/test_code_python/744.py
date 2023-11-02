def solution():
    yolanda_speed = 20  # Yolanda is riding her bike at 20 miles per hour
    husband_speed = 40  # Yolanda's husband is driving at 40 miles per hour
    time_difference = 1/4  # Yolanda's husband starts 15 minutes after Yolanda

    # Calculate the distance Yolanda travels before her husband starts
    distance_before_husband = yolanda_speed * time_difference

    # Calculate the time it takes for the husband to catch up with Yolanda
    time_to_catch_up = distance_before_husband / (husband_speed - yolanda_speed)

    # Convert the time to minutes
    time_to_catch_up_minutes = time_to_catch_up * 60

    result = time_to_catch_up_minutes
    return result

print(solution())