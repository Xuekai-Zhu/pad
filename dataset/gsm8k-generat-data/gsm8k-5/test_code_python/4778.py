def solution():
    initial_price = 600  # The phone's initial price was $600
    percent_off = 20  # Karsyn bought the phone at 20% of the initial price

    # Calculate the price Karsyn paid after negotiating
    price_after_negotiating = initial_price * (percent_off/100)

    result = price_after_negotiating
    return result

print(solution())