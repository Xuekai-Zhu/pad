def solution():
    friday_shipment = 1000
    saturday_sales = 300
    sunday_rotten = 200
    monday_shipment = 2 * friday_shipment

    # Calculate the total amount of tomatoes available for sale on Tuesday
    total_tomatoes = friday_shipment + monday_shipment - saturday_sales - sunday_rotten
    result = total_tomatoes
    return result

print(solution())