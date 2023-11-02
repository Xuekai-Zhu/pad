def solution():
    school_start_time = 8
    driving_time = 30
    time_stopped_for_red_lights = 3
    number_of_red_lights = 4
    time_waiting_for_construction = 10
    departure_time = 7.15

    total_time_stopped = time_stopped_for_red_lights * number_of_red_lights + time_waiting_for_construction
    total_driving_time = driving_time + total_time_stopped
    arrival_time = school_start_time + total_driving_time
    result = arrival_time - school_start_time
    return result

print(solution())