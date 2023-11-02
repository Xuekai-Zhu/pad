def solution():
    distance_from_house_to_sidewalk = 20
    distance_down_sidewalk = 200
    distance_left_to_intersection = distance_down_sidewalk * 2
    total_distance_so_far = distance_from_house_to_sidewalk + distance_down_sidewalk + distance_left_to_intersection
    distance_back_to_intersection = total_distance_so_far / 2
    total_distance = total_distance_so_far + distance_back_to_intersection
    result = total_distance
    return result

print(solution())