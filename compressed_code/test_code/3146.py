def solution():
    
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