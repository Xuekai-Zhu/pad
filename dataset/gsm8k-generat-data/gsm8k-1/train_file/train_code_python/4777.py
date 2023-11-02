def solution():
    """After negotiating for the price of a phone, Karsyn bought a phone at 20% of the initial price. If the phone's initial price was $600, calculate how much she paid after negotiating."""
    initial_price = 600
    discount = 0.2
    discounted_price = initial_price * (1 - discount)
    result = discounted_price
    return result

print(solution())