def solution():
    """A local bookshop is selling off its old inventory in order to bring in newer books. They currently have 743 books in their store. They sold 37 books in-store on Saturday and sold 128 books online. On Sunday, they sold twice as many books in-store and increased their online sales by 34 books. They also received a shipment of 160 books. How many books do they currently have?"""
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