def solution():
    """A store offers a $2 discount for every $10 purchase on any item in the store. Kataleya went to the store and bought 400 peaches sold at forty cents each. Calculate the total amount of money she paid at the store for the fruits."""
    # Define the cost of each peach
    PEACH_PRICE = 0.4

    # Calculate the total cost of peaches
    peach_cost = 400 * PEACH_PRICE

    # Calculate the number of $10 purchases
    num_purchases = peach_cost // 10

    # Calculate the total discount
    discount = num_purchases * 2

    # Calculate the total amount paid
    total_cost = peach_cost - discount

    # Display the total amount paid
    result = total_cost
    return result

print(solution())