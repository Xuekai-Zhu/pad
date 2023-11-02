def solution():
    distance_to_school = 2.5
    distance_to_market = 2
    num_round_trips_to_school = 4 * 2  # Two round trips per day, four days per week
    num_round_trips_to_market = 1  # One round trip per weekend
    total_distance = (distance_to_school * num_round_trips_to_school) + (distance_to_market * num_round_trips_to_market)
    weekly_mileage = total_distance * 2  # Round trip counts as two miles
    result = weekly_mileage
    return result

print(solution())