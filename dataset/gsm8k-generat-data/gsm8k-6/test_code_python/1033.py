def solution():
    calories_per_hour_walking = 300
    calories_per_hour_dancing = calories_per_hour_walking * 2 * 0.5 # James loses twice as many calories per hour as he did when he was walking and dances twice a day for .5 hours each time
    total_calories_lost = calories_per_hour_dancing * 4 # James dances 4 times a week
    result = total_calories_lost
    return result

print(solution())