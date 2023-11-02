def solution():
    flight_time = 11 * 60 + 20
    hours_reading = 2
    hours_watching = 4
    minutes_eating = 30
    minutes_radio = 40
    minutes_games = 70
    total_time = hours_reading + hours_watching + minutes_eating + minutes_radio + minutes_games
    time_left = flight_time - total_time
    hours_left = time_left // 60
    result = hours_left
    
    return result

print(solution())