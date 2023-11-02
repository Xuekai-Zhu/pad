def solution():
    """Maria bought a ticket to a ZOO. The regular price stands at $15, but she was able to get a 40% discount. How much did Maria pay for the ticket?"""
    regular_price = 15
    discount_percentage = 40
    discount = regular_price * discount_percentage / 100
    final_price = regular_price - discount
    result = final_price
    return result

print(solution())