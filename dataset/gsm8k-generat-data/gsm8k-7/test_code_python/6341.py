def solution():
    navigation_days = 21
    customs_days = 4
    transportation_days = 7
    expected_arrival_days = 2

    # Calculate the total number of days the shipment will be in transit
    total_transit_days = navigation_days + customs_days + transportation_days

    # Subtract the expected arrival days and add 2 (for today and tomorrow) to get the departure day
    departure_days_ago = total_transit_days - expected_arrival_days + 2
    result = departure_days_ago
    return result

print(solution())