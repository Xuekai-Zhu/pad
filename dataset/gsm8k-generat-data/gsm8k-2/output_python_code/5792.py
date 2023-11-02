def solution():
    """The dog toys Samantha buys for her dog are "buy one get one half off" and all cost $12.00 each. She buys 4 toys. How much does she spend on dog toys?"""
    toy_price = 12
    half_price = toy_price * 0.5
    # Samantha gets 1 free toy for every 2 toys she buys
    # So, she pays for 3 toys at full price and 1 at half price
    total_price = 3 * toy_price + 0.5 * half_price
    result = total_price * 4
    return result

print(solution())