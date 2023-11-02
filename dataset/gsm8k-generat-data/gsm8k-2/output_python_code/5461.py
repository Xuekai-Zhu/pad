def solution():
    """Ann can skate 6 miles an hour. Her friend Glenda can skate 8 miles an hour. If they start in the same place and skate in straight lines in opposite directions for 3 hours, how many miles apart do they end up?"""
    ann_speed = 6
    glenda_speed = 8
    total_time = 3
    total_distance = (ann_speed + glenda_speed) * total_time
    result = total_distance
    return result

print(solution())