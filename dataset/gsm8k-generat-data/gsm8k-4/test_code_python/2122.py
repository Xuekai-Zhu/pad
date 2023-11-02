def solution():
    """A salon has the same amount of customers every day. Each customer needs 1 can of hairspray during the styling and is also given 1 can of hairspray to take home. The salon also buys an extra 5 cans of hairspray each day to ensure there is never a shortage. If the salon buys 33 cans of hairspray every day, how many customers do they have each day?"""
    # Define the number of extra cans of hairspray purchased each day
    extra_cans = 5

    # Define the total number of cans used per customer
    total_cans = 2

    # Calculate the number of customers based on the number of cans purchased each day
    customers = (33 - extra_cans) / total_cans

    # Return the result
    result = int(customers)
    return result

print(solution())