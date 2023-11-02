def solution():
    # Define the initial stock of bicycles
    initial_stock = 0

    # Calculate the stock after Friday's sales and purchases
    friday_sales = 10
    friday_purchases = 15
    stock_friday = initial_stock + friday_purchases - friday_sales

    # Calculate the stock after Saturday's sales and purchases
    saturday_sales = 12
    saturday_purchases = 8
    stock_saturday = stock_friday + saturday_purchases - saturday_sales

    # Calculate the stock after Sunday's sales and purchases
    sunday_sales = 9
    sunday_purchases = 11
    stock_sunday = stock_saturday + sunday_purchases - sunday_sales

    # Calculate the net increase in stock
    net_increase = stock_sunday - initial_stock
    result = net_increase
    return result

print(solution())