def solution():
    """Willie came back from Europe with 70 euros. Normally 5 euros is worth 1 dollar, but the money exchange at the airport will only give Willie 5/7ths of the official exchange rate. How many dollars does Willie get?"""
    # Define the exchange rate of euros to dollars
    OFFICIAL_EXCHANGE_RATE = 5

    # Calculate how many dollars Willie would get at the official exchange rate
    official_dollars = 70 / OFFICIAL_EXCHANGE_RATE

    # Calculate how many dollars Willie actually gets at the airport exchange
    airport_rate = 5/7 * OFFICIAL_EXCHANGE_RATE
    actual_dollars = 70 / airport_rate

    # Display how many dollars Willie gets
    result = actual_dollars
    return result

print(solution())