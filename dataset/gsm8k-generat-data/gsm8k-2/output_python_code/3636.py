def solution():
    """Gretchen is a scuba diver. She likes to hunt for treasure on the ocean's floor, but when she finds something to keep, she must carry it back to the surface of the water to give it to her shipmate on the boat. She can only carry 3 objects at a time while she swims underwater. If she finds 17 objects underwater, what is the fewest number of trips to the surface of the water she must take to carry all 17 objects to the boat?"""
    objects_found = 17
    objects_per_trip = 3
    trips_needed = objects_found // objects_per_trip
    if objects_found % objects_per_trip != 0:
        trips_needed += 1
    result = trips_needed
    return result

print(solution())