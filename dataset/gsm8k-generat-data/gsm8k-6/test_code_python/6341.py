def solution():
    # Calculate the total number of days required for the shipment to reach the warehouse after departing Shanghai
    total_days = 21 + 4 + 7  # navigates for 21 days, regulatory processes take 4 days, and cargo takes 7 days to arrive at the warehouse
    days_left = 2  # shipment is expected in 2 days
    days_ago_departure = total_days - days_left
    result = days_ago_departure
    return result

print(solution())