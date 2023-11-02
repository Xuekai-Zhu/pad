def solution():
    """John buys 5 toys that each cost $3. He gets a 20% discount. How much did he pay for everything?"""
    num_toys = 5
    toy_cost = 3
    discount_percent = 20
    discount_amount = toy_cost * (discount_percent / 100)
    total_cost = (toy_cost - discount_amount) * num_toys
    result = total_cost
    return result

print(solution())