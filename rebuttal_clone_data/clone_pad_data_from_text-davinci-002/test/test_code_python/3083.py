def solution():
 
    ann_speed = 6
    glenda_speed = 8
    time = 3
    ann_distance = ann_speed * time
    glenda_distance = glenda_speed * time
    distance_apart = glenda_distance + ann_distance
    result = distance_apart
    return result

print(solution())