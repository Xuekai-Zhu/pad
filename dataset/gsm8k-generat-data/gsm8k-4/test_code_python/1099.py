def solution():
    """A hot dog stand sells 10 hot dogs every hour, each one selling for $2.  How many hours does the stand need to run to make $200 in sales?"""
    # Define the number of hot dogs sold per hour and the selling price of each hot dog
    HOT_DOGS_PER_HOUR = 10
    HOT_DOG_PRICE = 2

    # Define the target sales amount
    TARGET_SALES = 200

    # Initialize the running hour counter and the running sales total
    hours = 0
    sales = 0

    # Increment the sales and hour counters until the target sales amount is reached
    while sales < TARGET_SALES:
        # Increment the hour counter
        hours += 1

        # Calculate the sales for this hour
        hourly_sales = HOT_DOGS_PER_HOUR * HOT_DOG_PRICE

        # Add the sales to the running total
        sales += hourly_sales

    # Display the number of hours needed to reach the target sales amount
    result = hours
    return result

print(solution())