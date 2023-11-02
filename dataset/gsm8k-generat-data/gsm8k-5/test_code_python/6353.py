def solution():
    # Calculate the total distance each bird flew in 2 hours
    distance_eagle = 15 * 2  # Eagle can fly 15 miles per hour
    distance_falcon = 46 * 2  # Falcon can fly 46 miles per hour
    distance_pelican = 33 * 2  # Pelican can fly 33 miles per hour
    distance_hummingbird = 30 * 2  # Hummingbird can fly 30 miles per hour

    # Calculate the total distance all four birds flew in 2 hours
    total_distance = distance_eagle + distance_falcon + distance_pelican + distance_hummingbird
    result = total_distance
    return result

print(solution())