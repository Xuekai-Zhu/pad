def solution():
    
    shots_per_minute = 60 / 15
    seconds_shooting_per_shot = 5
    seconds_shooting_per_minute = shots_per_minute * seconds_shooting_per_shot
    result = seconds_shooting_per_minute
    return result

print(solution())