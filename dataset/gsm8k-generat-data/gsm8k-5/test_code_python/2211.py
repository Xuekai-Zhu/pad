def solution():
    distance_to_school = 2.5
    distance_to_market = 2
    school_round_trip = 2 * distance_to_school
    market_round_trip = 2 * distance_to_market
    school_trips_per_week = 2 * 4
    market_trips_per_week = 1
    total_weekly_distance = (school_round_trip * school_trips_per_week) + (market_round_trip * market_trips_per_week)
    result = total_weekly_distance
    return result

print(solution())