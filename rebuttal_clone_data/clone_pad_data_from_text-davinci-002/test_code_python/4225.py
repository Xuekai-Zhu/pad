def solution():
    seconds_per_shot = 15
    seconds_per_flame = 5
    shots_per_minute = 60 / seconds_per_shot
    seconds_flaming_per_minute = shots_per_minute * seconds_per_flame
    result = seconds_flaming_per_minute
    return result

print(solution())