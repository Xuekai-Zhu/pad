def solution():
    """Ann can skate 6 miles an hour. Her friend Glenda can skate 8 miles an hour. If they start in the same place and skate in straight lines in opposite directions for 3 hours, how many miles apart do they end up?"""
    ann_speed = 6
    glenda_speed = 8
    time = 3
    distance_ann = ann_speed * time
    distance_glenda = glenda_speed * time
    total_distance = distance_ann + distance_glenda
    result = total_distance
    return result

print(solution())