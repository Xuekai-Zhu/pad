def solution():
    # Define the distances
    school_distance = 2.5
    market_distance = 2

    # Calculate the round trip distance to school
    school_round_trip = school_distance * 2

    # Calculate the total round trip distance to school during the week
    weekly_school_distance = school_round_trip * 2 * 4

    # Calculate the round trip distance to the market
    market_round_trip = market_distance * 2

    # Calculate the total round trip distance to the market during the week
    weekly_market_distance = market_round_trip * 1

    # Calculate the total weekly mileage
    total_weekly_mileage = weekly_school_distance + weekly_market_distance

    result = total_weekly_mileage
    return result

print(solution())