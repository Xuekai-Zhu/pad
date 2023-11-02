def solution():
    
    flight_time = 10*60
    tv_episode_time = 3 * 25
    sleep_time = 4.5 * 60
    movie_time = 2 * 105
    total_time_spent = tv_episode_time + sleep_time + movie_time
    remaining_time = flight_time - total_time_spent
    result = remaining_time
    return result

print(solution())