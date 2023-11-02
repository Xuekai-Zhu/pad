def solution():
    current_inventory = 743  # The bookshop currently has 743 books
    saturday_sales = 37  # They sold 37 books in-store on Saturday
    online_sales_saturday = 128  # They sold 128 books online on Saturday
    sunday_sales = 2 * saturday_sales  # They sold twice as many books in-store on Sunday as on Saturday
    online_sales_sunday = online_sales_saturday + 34  # They increased their online sales by 34 books on Sunday
    books_received = 160  # They received a shipment of 160 books

    # Calculate the current inventory after the weekend
    current_inventory = current_inventory - (saturday_sales + sunday_sales) + online_sales_saturday + online_sales_sunday + books_received
    result = current_inventory
    return result

print(solution())