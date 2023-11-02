def solution():
    jenny_speed = 15
    anna_speed = 45
    start_time = 8*60  # convert start time to minutes
    jenny_arrival_time = start_time + (0.5*60)/jenny_speed  # add half hour jog time to start time
    anna_arrival_time = jenny_arrival_time + (anna_speed/jenny_speed)*(jenny_arrival_time - start_time)  # calculate when Anna catches up to Jenny
    travel_time = (anna_arrival_time - start_time)/60  # convert travel time from minutes to hours
    result = travel_time
    return result

print(solution())