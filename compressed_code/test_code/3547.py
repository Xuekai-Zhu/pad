def solution():
    
    initial_inventory = 743
    saturday_sales = 37
    online_sales_Saturday = 128
    sunday_sales_instore = 2*saturday_sales
    online_sales_Sunday = online_sales_Saturday + 34
    shipment = 160
    total_sales = saturday_sales + sunday_sales_instore + online_sales_Saturday + online_sales_Sunday
    current_inventory = initial_inventory - total_sales + shipment
    result = current_inventory
    return result

print(solution())