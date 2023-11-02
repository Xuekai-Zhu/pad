def solution():
    school_start_time = 8 * 60  # 8:00 AM in minutes
    normal_travel_time = 30  # minutes
    red_light_wait_time = 3  # minutes per red light
    num_red_lights = 4
    construction_wait_time = 10  # minutes
    departure_time = 7 * 60 + 15  # 7:15 AM in minutes

    # Calculate the total wait time for red lights
    total_red_light_wait_time = red_light_wait_time * num_red_lights

    # Calculate the total travel time
    total_travel_time = normal_travel_time + total_red_light_wait_time + construction_wait_time

    # Calculate the arrival time
    arrival_time = departure_time + total_travel_time

    # Calculate the number of minutes late
    minutes_late = arrival_time - school_start_time
    result = minutes_late
    return result

print(solution())