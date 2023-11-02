def solution():
    """A cargo ship moving from Shanghai to Vancouver navigates for 21 days before reaching port. Customs and regulatory processes in Vancouver last 4 days. Finally, moving the cargo from the port to your rural warehouse takes some time and it always arrives on the seventh day. How many days ago should the ship have departed if your warehouse is expecting the shipment 2 days from today?"""
    # Define the number of days for each step of the shipment process
    navigate_days = 21
    customs_days = 4
    warehouse_days = 7

    # Calculate the total number of days for the shipment process
    total_days = navigate_days + customs_days + warehouse_days

    # Calculate the number of days the shipment has been in transit
    transit_days = total_days - 2

    # Calculate the number of days ago the ship departed
    departure_days_ago = transit_days - total_days

    result = departure_days_ago
    return result

print(solution())