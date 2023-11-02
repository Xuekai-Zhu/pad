def solution():
    """Laura took six trips to park. On each trip, she spent 2 hours at the park and an additinal 30 minutes walking to and from the park. What percentage of the total time she took for her trips to the park did Laura spend in the park?"""
    park_time = 2
    walking_time = 0.5
    total_time_per_trip = park_time + walking_time
    total_trips = 6
    total_time = total_trips * total_time_per_trip
    park_time_total = park_time * total_trips
    percentage_in_park = (park_time_total / total_time) * 100
    result = percentage_in_park
    return result

print(solution())