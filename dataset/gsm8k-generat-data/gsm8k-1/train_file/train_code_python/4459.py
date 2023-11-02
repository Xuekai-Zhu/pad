def solution():
    """James buys a weight vest for $250. He then buys 200 pounds of weight plates for $1.2 per pound. A 200-pound weight vest would cost $700 but there is a $100 discount. How much does he save with his vest?"""
    vest_cost = 250
    plates_cost = 200 * 1.2
    full_vest_cost = 700
    discount = 100
    saved_amount = full_vest_cost - (vest_cost + plates_cost - discount)
    result = saved_amount
    return result

print(solution())