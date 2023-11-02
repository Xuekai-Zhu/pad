def solution():
    total_mileage = 10
    race_mileage = 4

    # Calculate the round-trip mileage between Layla's house and the high school
    round_trip_mileage = total_mileage - (2 * race_mileage)

    # Calculate the one-way mileage between Layla's house and the high school
    one_way_mileage = round_trip_mileage / 2
    result = one_way_mileage
    return result

print(solution())