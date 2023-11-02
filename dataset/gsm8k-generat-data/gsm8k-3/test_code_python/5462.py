def solution():
    """Ann can skate 6 miles an hour. Her friend Glenda can skate 8 miles an hour. If they start in the same place and skate in straight lines in opposite directions for 3 hours, how many miles apart do they end up?"""
    # Ann's speed in miles per hour
    ann_speed = 6

    # Glenda's speed in miles per hour
    glenda_speed = 8

    # Time in hours
    time = 3

    # Distance Ann skates
    ann_distance = ann_speed * time

    # Distance Glenda skates
    glenda_distance = glenda_speed * time

    # Total distance they end up apart
    total_distance = ann_distance + glenda_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())