def solution():
    """At Ken's local store, a pound of steak is going for $7. He decides to get two pounds. At the till, he pays using a $20 bill. How much money will he get back?"""
    steak_price_per_pound = 7
    pounds_of_steak = 2
    total_price = steak_price_per_pound * pounds_of_steak
    payment = 20
    change = payment - total_price
    result = change
    return result

print(solution())