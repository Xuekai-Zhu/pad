def solution():
    """Monica charges $25.00 per person when catering a dinner party. For repeat customers, she offers a 10% discount. Phoebe is a repeat customer who is having a dinner party for 20 guests. How much will Monica make from the party?"""
    guest_count = 20
    initial_price = 25 * guest_count
    repeat_discount = 0.1
    repeat_price = initial_price - (initial_price * repeat_discount)
    result = repeat_price
    return result

print(solution())