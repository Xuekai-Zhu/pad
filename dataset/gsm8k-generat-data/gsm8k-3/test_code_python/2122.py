def solution():
    """A salon has the same amount of customers every day. Each customer needs 1 can of hairspray during the styling and is also given 1 can of hairspray to take home. The salon also buys an extra 5 cans of hairspray each day to ensure there is never a shortage. If the salon buys 33 cans of hairspray every day, how many customers do they have each day?"""
    # Define the number of cans of hairspray used per customer
    SPRAY_PER_CUSTOMER = 2

    # Define the number of extra cans of hairspray bought each day
    EXTRA_SPRAY = 5

    # Calculate the number of customers per day
    customers_per_day = (33 - EXTRA_SPRAY) / SPRAY_PER_CUSTOMER

    # Display the number of customers per day
    result = customers_per_day
    return result

print(solution())