def solution():
    """Last week, the price of a movie ticket was $100. This year the price is down by 20%. What's the new price of the movie ticket?"""
    # Define the original ticket price
    original_price = 100

    # Calculate the new ticket price after the 20% discount
    new_price = original_price - (original_price * 0.2)

    # Display the new ticket price
    result = new_price
    return result

print(solution())