def solution():
    # Calculate the total number of days needed for the shipment to arrive at the warehouse
    total_days = 21 + 4 + 7 + 2

    # Subtract the total number of days from today to find the departure date
    departure_date = total_days - 2
    result = departure_date
    return result

print(solution())