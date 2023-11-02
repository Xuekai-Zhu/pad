def solution():
    
    flight_time = 10 * 60  
    tv_time = 3 * 25
    sleep_time = 4.5 * 60  
    movie_time = 2 * 105  
    total_time = tv_time + sleep_time + movie_time
    time_left = flight_time - total_time
    result = time_left
    return result

print(solution())