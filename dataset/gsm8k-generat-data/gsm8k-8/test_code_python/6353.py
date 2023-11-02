def solution():
    # Define the speeds of the four birds
    eagle_speed = 15
    falcon_speed = 46
    pelican_speed = 33
    hummingbird_speed = 30

    # Calculate the distance each bird flew in 2 hours
    eagle_distance = eagle_speed * 2
    falcon_distance = falcon_speed * 2
    pelican_distance = pelican_speed * 2
    hummingbird_distance = hummingbird_speed * 2

    # Calculate the total distance all the birds flew
    total_distance = eagle_distance + falcon_distance + pelican_distance + hummingbird_distance
    result = total_distance
    return result

print(solution())