def solution():
    """Danivan Drugstore has 4500 bottles of hand sanitizer gel in inventory at the beginning of the week. On Monday 2445 bottles were sold, on Tuesday 900 bottles were sold, and 50 bottles each day for the rest of the week were sold (from Wednesday until Sunday). On Saturday, the supplier delivers an order for 650 bottles. How many bottles of sanitizer gel does the Drugstore have at the end of the week?"""
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