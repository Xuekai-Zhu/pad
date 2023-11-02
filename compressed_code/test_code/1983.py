def solution():
    
    bald_eagle_speed = 100
    peregrine_falcon_speed = 2 * bald_eagle_speed
    bald_eagle_time = 30
    distance = bald_eagle_speed * (bald_eagle_time / 60 / 60)
    peregrine_falcon_time = distance / peregrine_falcon_speed * 60 * 60
    result = peregrine_falcon_time
    return result

print(solution())