def solution():
    
    bus_capacity = 200
    first_trip = bus_capacity * 3/4
    return_trip = bus_capacity * 4/5
    total_people = first_trip + return_trip
    result = total_people
    return result

print(solution())