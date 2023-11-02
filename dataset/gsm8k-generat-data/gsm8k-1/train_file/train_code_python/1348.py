def solution():
    """Emerson and his friends love rowing and don't miss the sport on weekends. Starting in the morning, Emerson rowed and was 6 miles away from his starting point on a particular weekend. He continued for another 15 miles at a constant speed, only stopping for a while for rest before covering the remaining 18 miles. What's the total distance covered by Emerson on his trip?"""
    distance_from_start = 6
    second_leg_distance = 15
    final_leg_distance = 18
    total_distance = distance_from_start + second_leg_distance + final_leg_distance
    result = total_distance
    return result

print(solution())