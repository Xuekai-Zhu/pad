def solution():
    """John visits his parents twice a month. It takes him 2 hours to drive there at a speed of 70 mph. Considering the round trip, how many miles a month does he drive when visiting his parents?"""
    visits_per_month = 2
    time_per_visit = 2
    speed = 70
    distance_per_visit = time_per_visit * speed
    round_trip_distance = distance_per_visit * 2
    total_distance = round_trip_distance * visits_per_month
    result = total_distance
    return result

print(solution())