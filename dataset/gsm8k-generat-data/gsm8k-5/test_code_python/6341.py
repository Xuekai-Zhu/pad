def solution():
    navigation_days = 21  # Days spent navigating from Shanghai to Vancouver
    customs_days = 4  # Days spent in customs and regulatory processes in Vancouver
    transportation_days = 7  # Days taken to move the cargo from port to warehouse
    total_days = navigation_days + customs_days + transportation_days  # Total days taken for the shipment to arrive

    # Calculate the number of days ago the ship should have departed
    days_ago_departure = total_days - 2  # The warehouse is expecting the shipment in 2 days from today

    result = days_ago_departure
    return result

print(solution())