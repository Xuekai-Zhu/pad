def solution():
    """An eagle can fly 15 miles per hour; a falcon can fly 46 miles per hour; a pelican can fly 33 miles per hour; a hummingbird can fly 30 miles per hour. If the eagle, the falcon, the pelican, and the hummingbird flew for 2 hours straight, how many miles in total did the birds fly?"""
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