def solution():
    """Willie came back from Europe with 70 euros. Normally 5 euros is worth 1 dollar, but the money exchange at the airport will only give Willie 5/7ths of the official exchange rate. How many dollars does Willie get?"""
    # Define the exchange rate between euros and dollars
    official_rate = 5  # 5 euros = 1 dollar

    # Calculate the exchange rate Willie gets at the airport
    airport_rate = (5/7) * official_rate

    # Convert Willie's Euros to dollars using the airport exchange rate
    euros = 70
    dollars = euros * airport_rate

    # return the result in dollars
    result = dollars
    return result

print(solution())