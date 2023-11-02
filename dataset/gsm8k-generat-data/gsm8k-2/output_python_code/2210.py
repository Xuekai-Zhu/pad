def solution():
    """The trip from Philip's house to the children's school is 2.5 miles, and the trip to the market is 2 miles. He makes the round trip to school two times (when taking the children to school and when bringing them back) every day for 4 days a week. Then he makes a round trip to the market once during weekends. What is his car's mileage for a typical week?"""
    school_trip = 2 * 2.5
    market_trip = 2 * 2
    school_weekly_trip = school_trip * 4 * 2
    market_weekly_trip = market_trip * 2
    total_distance = school_weekly_trip + market_weekly_trip
    result = total_distance
    return result

print(solution())