def solution():
    """A cargo ship moving from Shanghai to Vancouver navigates for 21 days before reaching port. Customs and regulatory processes in Vancouver last 4 days. Finally, moving the cargo from the port to your rural warehouse takes some time and it always arrives on the seventh day. How many days ago should the ship have departed if your warehouse is expecting the shipment 2 days from today?"""
    voyage_time = 21
    customs_time = 4
    delivery_time = 7
    total_time = voyage_time + customs_time + delivery_time
    expected_delivery_date = total_time + 2  # add 2 days from today
    departure_date = expected_delivery_date - total_time
    days_ago = departure_date - 2  # subtract 2 days to get "days ago"
    result = days_ago
    return result

print(solution())