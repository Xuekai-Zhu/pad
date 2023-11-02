def solution():
    """Laura took six trips to park. On each trip, she spent 2 hours at the park and an additional 30 minutes walking to and from the park. What percentage of the total time she took for her trips to the park did Laura spend in the park?"""
    trips_to_park = 6
    time_at_park = 2
    walking_time = 0.5
    total_time = (time_at_park + walking_time) * trips_to_park
    percent_at_park = (time_at_park * trips_to_park / total_time) * 100
    result = percent_at_park
    
    return result

print(solution())