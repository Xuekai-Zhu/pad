def solution():
    tamika_hours = 8
    tamika_speed = 45
    logan_hours = 5
    logan_speed = 55
    tamika_distance = tamika_hours * tamika_speed
    logan_distance = logan_hours * logan_speed
    difference = tamika_distance - logan_distance
    result = abs(difference)
    
    return result

print(solution())