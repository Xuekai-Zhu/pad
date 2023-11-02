def solution():
    janet_speed = 30
    sister_speed = 12
    lake_width = 60

    # Calculate the time it takes for Janet to cross the lake
    janet_time = lake_width / janet_speed

    # Calculate the distance the sister needs to cover to catch up with Janet
    distance_to_cover = lake_width

    # Calculate the relative speed between Janet and her sister
    relative_speed = janet_speed - sister_speed

    # Calculate the time it takes for the sister to catch up with Janet
    time_to_catch_up = distance_to_cover / relative_speed

    # Calculate the total time that Janet has to wait for her sister to catch up
    total_time = janet_time + time_to_catch_up
    result = total_time
    return result

print(solution())