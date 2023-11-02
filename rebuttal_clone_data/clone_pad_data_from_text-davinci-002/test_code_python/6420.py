def solution():
    distance_1 = 20
    distance_2 = 200
    distance_3 = distance_1 + distance_2
    distance_4 = 2 * distance_3
    distance_5 = 0.5 * (distance_1 + distance_2 + distance_3 + distance_4)
    total_distance = 2 * (distance_1 + distance_2 + distance_3 + distance_4 + distance_5)
    result = total_distance
    return result

print(solution())