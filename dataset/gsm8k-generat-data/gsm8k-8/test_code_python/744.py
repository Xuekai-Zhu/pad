def solution():
    # Convert Yolanda's start time to minutes
    yolanda_start_time = 7 * 60

    # Calculate Yolanda's distance covered in the time it takes her husband to leave
    yolanda_distance_before_lunch = 20 * (15/60)

    # Calculate the time it will take Yolanda's husband to catch up with her
    time_to_catch_up = yolanda_distance_before_lunch / (40 - 20) * 60

    # Add the time it takes for Yolanda's husband to catch up to Yolanda's start time to get the total time
    total_time = yolanda_start_time + time_to_catch_up

    # Convert the total time to hours and minutes
    hours = total_time // 60
    minutes = total_time % 60

    # Return the time it takes for Yolanda's husband to catch up with Yolanda in minutes
    result = minutes
    return result

print(solution())