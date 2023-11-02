def solution():
    speed_bald_eagle = 100
    speed_peregrine_falcon = speed_bald_eagle * 2
    time_bald_eagle = 30
    distance_traveled = speed_bald_eagle * time_bald_eagle
    time_peregrine_falcon = distance_traveled / speed_peregrine_falcon
    result = time_peregrine_falcon
    return result

print(solution())