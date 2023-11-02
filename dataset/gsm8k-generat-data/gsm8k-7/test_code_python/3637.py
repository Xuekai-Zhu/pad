def solution():
    num_objects = 17
    objects_per_trip = 3

    # Calculate the total number of trips needed to carry all objects to the surface
    num_trips = num_objects / objects_per_trip

    # If there are leftover objects, add an additional trip
    if num_objects % objects_per_trip != 0:
        num_trips += 1
    
    result = num_trips
    return result

print(solution())