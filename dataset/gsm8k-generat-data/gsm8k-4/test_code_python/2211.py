def solution():
    """The trip from Philip's house to the children's school is 2.5 miles, and the trip to the market is 2 miles. He makes the round trip to school two times (when taking the children to school and when bringing them back) every day for 4 days a week. Then he makes a round trip to the market once during weekends. What is his car's mileage for a typical week?"""
    # Define the distance to the school and market
    school_distance = 2.5
    market_distance = 2

    # Define the number of round trips to school per week
    school_trips_per_week = 2 * 4

    # Define the number of round trips to the market per week
    market_trips_per_week = 1

    # Calculate the total distance traveled to school per week
    school_distance_per_week = school_distance * school_trips_per_week

    # Calculate the total distance traveled to the market per week
    market_distance_per_week = market_distance * market_trips_per_week

    # Calculate the total mileage for a typical week
    total_mileage = school_distance_per_week + market_distance_per_week

    result = total_mileage
    return result

print(solution())