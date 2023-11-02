def solution():
    
    friday_shipment = 1000
    saturday_sales = 300
    sunday_waste = 200
    monday_shipment = 2 * friday_shipment
    total_tomatoes = friday_shipment - saturday_sales - sunday_waste + monday_shipment
    result = total_tomatoes
    return result

print(solution())