def solution():
    time = half_hour
    Polly_laps = 12
    Polly_time = time
    Gerald_laps = Polly_laps / 2
    Gerald_time = Gerald_laps * Polly_time 
    track_length = 1/4
    Polly_speed = track_length / Polly_time
    Gerald_speed = track_length / Gerald_time
    result = Gerald_speed
    
    return result

print(solution())