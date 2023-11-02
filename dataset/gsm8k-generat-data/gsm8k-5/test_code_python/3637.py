def solution():
    objects_found = 17  # Gretchen finds 17 objects underwater
    objects_per_trip = 3  # Gretchen can carry 3 objects in one trip to the surface
    trips_needed = objects_found // objects_per_trip  # Calculate the number of trips Gretchen needs to make
    if objects_found % objects_per_trip != 0:  # If there are objects left over after making the full trips
        trips_needed += 1  # Add one more trip to get the remaining objects to the surface
    result = trips_needed
    return result

print(solution())