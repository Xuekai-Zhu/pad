def solution():
    """A cargo ship moving from Shanghai to Vancouver navigates for 21 days before reaching port.
    Customs and regulatory processes in Vancouver last 4 days. Finally, moving the cargo from the 
    port to your rural warehouse takes some time and it always arrives on the seventh day. 
    How many days ago should the ship have departed if your warehouse is expecting the shipment 2 days from today?"""
    navigation_time = 21
    customs_time = 4
    warehouse_time = 7
    total_time = navigation_time + customs_time + warehouse_time
    expected_arrival = 2
    days_ago_ship_departed = total_time - expected_arrival
    result = days_ago_ship_departed
    return result

print(solution())