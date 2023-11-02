def solution():
    ann_speed = 6  # miles per hour
    glenda_speed = 8  # miles per hour
    time = 3  # hours

    # Calculate the total distance that Ann travels
    ann_distance = ann_speed * time

    # Calculate the total distance that Glenda travels
    glenda_distance = glenda_speed * time

    # Calculate the distance between them at the end of 3 hours
    total_distance = ann_distance + glenda_distance
    result = total_distance
    return result

print(solution())