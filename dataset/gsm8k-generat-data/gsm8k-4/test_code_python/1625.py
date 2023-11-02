def solution():
    """Last week, the price of a movie ticket was $100. This year the price is down by 20%. What's the new price of the movie ticket?"""
    # Define the initial price of the movie ticket
    initial_price = 100

    # Calculate the price after the 20% decrease
    new_price = initial_price - (initial_price * 0.2)

    # return the result
    result = new_price
    return result

print(solution())