def solution():
    """A cargo ship moving from Shanghai to Vancouver navigates for 21 days before reaching port. Customs and regulatory processes in Vancouver last 4 days. Finally, moving the cargo from the port to your rural warehouse takes some time and it always arrives on the seventh day. How many days ago should the ship have departed if your warehouse is expecting the shipment 2 days from today?"""
    # Define the number of days for each stage of the shipment
    SHIPPING_DAYS = 21
    CUSTOMS_DAYS = 4
    DELIVERY_DAYS = 7

    # Calculate the total number of days for the shipment
    total_days = SHIPPING_DAYS + CUSTOMS_DAYS + DELIVERY_DAYS

    # Determine how many days ago the ship should have departed
    days_ago_departed = total_days - 2

    # Display the number of days ago the ship should have departed
    result = days_ago_departed
    return result

print(solution())