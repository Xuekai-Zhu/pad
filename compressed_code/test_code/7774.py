def solution():
    
    sadie_time = 2
    sadie_speed = 3
    ariana_time = 0.5
    ariana_speed = 6
    sarah_speed = 4
    total_time = 4.5
    
    
    sadie_distance = sadie_time * sadie_speed
    ariana_distance = ariana_time * ariana_speed
    sarah_distance = (total_time - sadie_time - ariana_time) * sarah_speed
    
    
    total_distance = sadie_distance + ariana_distance + sarah_distance
    result = total_distance
    
    return result

print(solution())