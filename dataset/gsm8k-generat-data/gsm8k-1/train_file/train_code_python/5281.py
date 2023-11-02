def solution():
    """Willie came back from Europe with 70 euros. Normally 5 euros is worth 1 dollar, but the money exchange at the airport will only give Willie 5/7ths of the official exchange rate. How many dollars does Willie get?"""
    euros = 70
    exchange_rate = 5/1
    airport_rate = 5/7 * exchange_rate
    dollars_received = euros * airport_rate
    result = dollars_received
    return result

print(solution())