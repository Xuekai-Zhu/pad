def solution():
    """After negotiating for the price of a phone, Karsyn bought a phone at 20% of the initial price. If the phone's initial price was $600, calculate how much she paid after negotiating."""
    # Define the initial price of the phone
    initial_price = 600

    # Calculate the negotiated price
    negotiated_price = initial_price * 0.2

    # Calculate the final price paid
    final_price = initial_price - negotiated_price

    # return the result
    result = final_price
    return result

print(solution())