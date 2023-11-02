def solution():
    distance_1 = x  # The distance Rick traveled from the start to his first destination
    distance_2 = 2 * distance_1  # The distance Rick traveled from the first to the second destinations
    distance_3 = 40  # The distance Rick traveled from the second to the third destination
    distance_4 = 2 * (distance_1 + distance_2 + distance_3)  # The distance Rick traveled from the third to the final destination
    total_distance = distance_1 + distance_2 + distance_3 + distance_4
    result = total_distance
    return result

print(solution())