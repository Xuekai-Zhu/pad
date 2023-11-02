def solution():
    """An eagle can fly 15 miles per hour; a falcon can fly 46 miles per hour; a pelican can fly 33 miles per hour; a hummingbird can fly 30 miles per hour. If the eagle, the falcon, the pelican, and the hummingbird flew for 2 hours straight, how many miles in total did the birds fly?"""
    # Define the speeds of the birds
    eagle_speed = 15
    falcon_speed = 46
    pelican_speed = 33
    hummingbird_speed = 30

    # Define the time the birds flew
    time = 2

    # Calculate the total distance each bird flew
    eagle_distance = eagle_speed * time
    falcon_distance = falcon_speed * time
    pelican_distance = pelican_speed * time
    hummingbird_distance = hummingbird_speed * time

    # Calculate the total distance all the birds flew
    total_distance = eagle_distance + falcon_distance + pelican_distance + hummingbird_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())