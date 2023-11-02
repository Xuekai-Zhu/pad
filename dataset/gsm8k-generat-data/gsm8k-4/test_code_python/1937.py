def solution():
    """On Friday, Hank opened his used-bicycle store with a stock of bicycles, all fixed-up and ready to ride. Over the course of the day, he sold 10 bicycles and bought an additional 15 to fix up. On Saturday, he sold 12 bicycles and bought 8 more. And on Sunday, he sold 9 bicycles and bought 11 more. What was the net increase in the number of bicycles in stock in Hank's store over the three days?"""

    # Define the initial stock of bicycles
    initial_stock = None

    # On Friday, Hank sold 10 bicycles and bought 15 more to fix up
    friday_sales = 10
    friday_purchases = 15

    # Calculate the number of bicycles in stock after Friday
    stock_after_friday = initial_stock + friday_purchases - friday_sales

    # On Saturday, Hank sold 12 bicycles and bought 8 more
    saturday_sales = 12
    saturday_purchases = 8

    # Calculate the number of bicycles in stock after Saturday
    stock_after_saturday = stock_after_friday + saturday_purchases - saturday_sales

    # On Sunday, Hank sold 9 bicycles and bought 11 more
    sunday_sales = 9
    sunday_purchases = 11

    # Calculate the number of bicycles in stock after Sunday
    stock_after_sunday = stock_after_saturday + sunday_purchases - sunday_sales

    # Calculate the net increase in the number of bicycles in stock
    net_increase = stock_after_sunday - initial_stock

    # return the result
    result = net_increase
    return result

print(solution())