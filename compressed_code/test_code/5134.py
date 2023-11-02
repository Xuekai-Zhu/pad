def solution():
    
    starting_inventory = 4500
    monday_sales = 2445
    tuesday_sales = 900
    daily_sales = 50
    weekend_sales = daily_sales * 5
    supplier_delivery = 650

    total_sales = monday_sales + tuesday_sales + weekend_sales
    ending_inventory = starting_inventory - total_sales + supplier_delivery
    result = ending_inventory
    return result

print(solution())