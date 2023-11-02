def solution():
    
    current_inventory = 743
    saturday_sales = 37
    online_sales_saturday = 128
    sunday_sales = 2 * saturday_sales
    online_sales_sunday = online_sales_saturday + 34
    shipment = 160
    total_sales = saturday_sales + sunday_sales + online_sales_saturday + online_sales_sunday
    new_inventory = current_inventory - total_sales + shipment
    result = new_inventory
    return result

print(solution())