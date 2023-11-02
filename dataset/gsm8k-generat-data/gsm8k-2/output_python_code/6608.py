def solution():
    """John buys 5 toys that each cost $3. He gets a 20% discount. How much did he pay for everything?"""
    toy_price = 3
    num_toys = 5
    discount_percent = 20
    discount_price = toy_price * (1 - (discount_percent / 100))
    total_price = num_toys * discount_price
    result = total_price
    return result

print(solution())