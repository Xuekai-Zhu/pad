def solution():
    
    eagle_speed = 15
    falcon_speed = 46
    pelican_speed = 33
    hummingbird_speed = 30
    total_time = 2
    eagle_distance = eagle_speed * total_time
    falcon_distance = falcon_speed * total_time
    pelican_distance = pelican_speed * total_time
    hummingbird_distance = hummingbird_speed * total_time
    total_distance = eagle_distance + falcon_distance + pelican_distance + hummingbird_distance
    result = total_distance
    return result

print(solution())