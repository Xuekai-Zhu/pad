def solution():
    school_distance = 20
    supermarket_distance = 10
    round_trip_distance = school_distance + (supermarket_distance * 2)
    days_per_week = 5
    number_of_trips = 2
    weekly_mileage = (round_trip_distance * number_of_trips) * days_per_week
    result = weekly_mileage
    return result

print(solution())