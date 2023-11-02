def solution():
    """A local bookshop is selling off its old inventory in order to bring in newer books. They currently have 743 books in their store. They sold 37 books in-store on Saturday and sold 128 books online. On Sunday, they sold twice as many books in-store and increased their online sales by 34 books. They also received a shipment of 160 books. How many books do they currently have?"""
    # Define the starting inventory and sales
    starting_inventory = 743
    saturday_sales = 37
    online_sales_sat = 128
    sunday_sales_instore = saturday_sales * 2
    online_sales_sun = online_sales_sat + 34
    new_inventory = 160
    
    # Calculate the total sales and ending inventory
    total_sales = saturday_sales + online_sales_sat + sunday_sales_instore + online_sales_sun
    ending_inventory = starting_inventory - total_sales + new_inventory
    
    # Display the ending inventory
    result = ending_inventory
    return result

print(solution())