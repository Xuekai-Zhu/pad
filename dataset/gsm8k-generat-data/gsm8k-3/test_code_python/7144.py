def solution():
    """The price of an iPhone fell 10% in a particular month and another 20% in the second month.  If the initial price was $1000, calculate the price after the second month."""
    # Define the initial price of the iPhone
    initial_price = 1000

    # Calculate the price after the first month
    price_first_month = initial_price * 0.9

    # Calculate the price after the second month
    price_second_month = price_first_month * 0.8

    # Display the price after the second month
    result = price_second_month
    return result

print(solution())