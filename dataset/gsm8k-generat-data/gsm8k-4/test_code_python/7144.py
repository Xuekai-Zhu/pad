def solution():
    """The price of an iPhone fell 10% in a particular month and another 20% in the second month. If the initial price was $1000, calculate the price after the second month."""
    # Define the initial price
    initial_price = 1000

    # Calculate the price after the first month
    first_month_price = initial_price * 0.9

    # Calculate the price after the second month
    second_month_price = first_month_price * 0.8

    # Return the result
    result = second_month_price
    return result

print(solution())