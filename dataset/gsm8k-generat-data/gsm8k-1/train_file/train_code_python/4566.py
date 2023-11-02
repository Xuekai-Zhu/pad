def solution():
    """A local bookshop is selling off its old inventory in order to bring in newer books. They currently have 743 books in their store. They sold 37 books in-store on Saturday and sold 128 books online. On Sunday, they sold twice as many books in-store and increased their online sales by 34 books. They also received a shipment of 160 books. How many books do they currently have?"""
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