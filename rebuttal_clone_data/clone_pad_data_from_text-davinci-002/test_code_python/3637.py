def solution():
    objects_to_carry = 17
    objects_per_trip = 3
    total_trips = objects_to_carry / objects_per_trip
    result = math.ceil(total_trips)
    return result

print(solution())