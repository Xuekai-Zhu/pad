def solution():
    
    bald_eagle_speed = 100 
    peregrine_falcon_speed = 2 * bald_eagle_speed 
    bald_eagle_time = 30 
    distance = (bald_eagle_speed * bald_eagle_time) / 3600 
    peregrine_falcon_time = (distance * 3600) / peregrine_falcon_speed 
    result = peregrine_falcon_time
    return result

print(solution())