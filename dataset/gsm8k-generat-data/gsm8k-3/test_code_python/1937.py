def solution():
    """On Friday, Hank opened his used-bicycle store with a stock of bicycles, all fixed-up and ready to ride. Over the course of the day, he sold 10 bicycles and bought an additional 15 to fix up. On Saturday, he sold 12 bicycles and bought 8 more. And on Sunday, he sold 9 bicycles and bought 11 more. What was the net increase in the number of bicycles in stock in Hank's store over the three days?"""
    # Define the initial stock of bicycles
    initial_stock = 0

    # Calculate the stock of bicycles after Friday
    friday_stock = initial_stock - 10 + 15

    # Calculate the stock of bicycles after Saturday
    saturday_stock = friday_stock - 12 + 8

    # Calculate the stock of bicycles after Sunday
    sunday_stock = saturday_stock - 9 + 11

    # Calculate the net increase in the number of bicycles in stock
    net_increase = sunday_stock - initial_stock

    # Display the net increase
    result = net_increase
    return result

print(solution())