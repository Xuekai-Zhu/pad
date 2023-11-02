def solution():
    """Blake bought 4 lollipops and 6 packs of chocolate. If each lollipop costs $2 and a pack of chocolate costs the same as four lollipops, how much change will Blake get back if he gave the cashier 6 $10 bills?"""
    num_lollipops = 4
    num_chocolate = 6
    lollipop_price = 2
    chocolate_price = lollipop_price * 4

    total_cost = (num_lollipops * lollipop_price) + (num_chocolate * chocolate_price)
    total_payment = 6 * 10
    change = total_payment - total_cost
    result = change

    return result

print(solution())