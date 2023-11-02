def solution():
    people_waiting = 84
    cars_available = 7
    seats_per_car = 2
    people_per_trip = cars_available * seats_per_car
    trips_needed = people_waiting / people_per_trip
    result = trips_needed
    return result

print(solution())