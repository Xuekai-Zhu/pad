def solution():
    
    fire_rate = 15
    flame_duration = 5
    shots_per_minute = 60 / fire_rate
    seconds_of_flame_per_shot = flame_duration
    seconds_of_flame_per_minute = shots_per_minute * seconds_of_flame_per_shot
    result = seconds_of_flame_per_minute
    return result

print(solution())