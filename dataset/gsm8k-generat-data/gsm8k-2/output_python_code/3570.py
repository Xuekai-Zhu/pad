def solution():
    """Vins rides his bike 6 miles to school. He rides home a different route that is 7 miles long. This week, Vins rode to school and back 5 times. How many miles did Vins ride his bike this week?"""
    distance_to_school = 6
    distance_from_school = 7
    trips_per_week = 5
    total_distance = (distance_to_school + distance_from_school) * trips_per_week
    result = total_distance
    return result

print(solution())