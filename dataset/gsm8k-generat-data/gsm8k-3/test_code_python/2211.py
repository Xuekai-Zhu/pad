def solution():
    """The trip from Philip's house to the children's school is 2.5 miles, and the trip to the market is 2 miles. He makes the round trip to school two times (when taking the children to school and when bringing them back) every day for 4 days a week. Then he makes a round trip to the market once during weekends. What is his car's mileage for a typical week?"""
    # Define the distance of each trip
    SCHOOL_TRIP = 2.5
    MARKET_TRIP = 2

    # Define the number of round trips to school and market each week
    SCHOOL_TRIPS_PER_WEEK = 2 * 2 * 4  # 2 round trips per day, 4 days per week
    MARKET_TRIPS_PER_WEEK = 2

    # Calculate the total distance traveled in a week
    total_distance = (SCHOOL_TRIP * SCHOOL_TRIPS_PER_WEEK) + (MARKET_TRIP * MARKET_TRIPS_PER_WEEK)

    # Display the car's mileage for a typical week
    result = total_distance
    return result

print(solution())