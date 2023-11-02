def solution(): 
    sadie_time = 2
    ariana_time = .5
    sarah_time= 4.5
    sadie_speed = 3
    ariana_speed = 6
    sarah_speed = 4
    total_time = sadie_time+ariana_time+sarah_time
    sadie_distance = sadie_time*sadie_speed
    ariana_distance = ariana_time*ariana_speed
    sarah_distance = sarah_time*sarah_speed
    total_distance=sadie_distance+ariana_distance+sarah_distance
    result = total_distance
    return result

print(solution())