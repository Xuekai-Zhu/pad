def solution():
    """Juanita goes through 1 bottle of sunscreen a month.  She likes to stock up for the entire year when a certain website offers 30% off her entire purchase.  If each bottle is $30.00 how much will all of the sunscreen cost after the discount?"""
    # Define the cost of one bottle of sunscreen
    SUNSCREEN_COST = 30.00

    # Define the number of bottles Juanita needs for the year
    bottles_needed = 12

    # Calculate the total cost of the sunscreen without the discount
    total_cost_before_discount = bottles_needed * SUNSCREEN_COST

    # Calculate the discounted price
    discounted_price = total_cost_before_discount * 0.7

    # Display the discounted price
    result = discounted_price
    return result

print(solution())