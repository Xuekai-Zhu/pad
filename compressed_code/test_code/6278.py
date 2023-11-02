def solution():
    
    capacity = 200
    first_trip = capacity * (3/4)
    return_trip = capacity * (4/5)
    total_people = first_trip + return_trip
    result = total_people
    return result

print(solution())