def solution():
    
    objects_found = 17
    objects_per_trip = 3
    trips_to_surface = objects_found // objects_per_trip
    if objects_found % objects_per_trip != 0:
        trips_to_surface += 1
    result = trips_to_surface
    return result

print(solution())