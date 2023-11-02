def solution():
    eagle_mph = 15
    falcon_mph = 46
    pelican_mph = 33
    hummingbird_mph = 30
    total_hours = 2
    eagle_distance = eagle_mph * total_hours
    falcon_distance = falcon_mph * total_hours
    pelican_distance = pelican_mph * total_hours
    hummingbird_distance = hummingbird_mph * total_hours
    total_distance = eagle_distance + falcon_distance + pelican_distance + hummingbird_distance
    result = total_distance
    
    return result

print(solution())