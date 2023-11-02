def solution():
    eagle_speed = 15
    falcon_speed = 46
    pelican_speed = 33
    hummingbird_speed = 30
    time = 2
    
    # Calculate the total distance each bird traveled in 2 hours
    eagle_distance = eagle_speed * time
    falcon_distance = falcon_speed * time
    pelican_distance = pelican_speed * time
    hummingbird_distance = hummingbird_speed * time
    
    # Calculate the total distance of all the birds
    total_distance = eagle_distance + falcon_distance + pelican_distance + hummingbird_distance
    result = total_distance
    return result

print(solution())