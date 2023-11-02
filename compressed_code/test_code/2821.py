def solution():
    
    objects_found = 17
    objects_per_trip = 3
    trips_needed = objects_found // objects_per_trip
    if objects_found % objects_per_trip != 0:
        trips_needed += 1
    result = trips_needed
    return result

print(solution())