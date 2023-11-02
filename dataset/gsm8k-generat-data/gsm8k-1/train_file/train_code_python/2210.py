def solution():
    """The trip from Philip's house to the children's school is 2.5 miles, and the trip to the market is 2 miles. He makes the round trip to school two times (when taking the children to school and when bringing them back) every day for 4 days a week. Then he makes a round trip to the market once during weekends. What is his car's mileage for a typical week?"""
    school_trip_distance = 2.5
    market_trip_distance = 2
    roundtrips_to_school_per_day = 2
    days_of_school_per_week = 4
    roundtrips_to_market_per_weekend = 1
    total_miles = (school_trip_distance * roundtrips_to_school_per_day * days_of_school_per_week) + (market_trip_distance * roundtrips_to_market_per_weekend * 2)
    result = total_miles
    return result

print(solution())